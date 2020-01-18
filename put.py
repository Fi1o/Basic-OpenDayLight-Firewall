import requests
import json
import sys

from ctypes import *


class go_string(Structure):
    _fields_ = [
        ("p", c_char_p),
        ("n", c_int)]

#flowgen is used to call the go code
flowgen = cdll.LoadLibrary("./buildflow.so")

src = str(sys.argv[1])+'/32'
dst = str(sys.argv[2])+'/32'

Src = src.encode('utf-8')
Dst = dst.encode('utf-8')

SSr = go_string(c_char_p(Src), len(Src))
DDs = go_string(c_char_p(Dst), len(Dst))

flowgen.Goflowgo(SSr,DDs)

xmlfile = "flow.xml"
headers = {'content-type': 'application/xml'}
with open(xmlfile) as xml:
    responce2 = requests.post("http://192.168.56.106:8181/restconf/operations/sal-flow:add-flow",data=xml,headers=headers,auth=('admin','admin'))
statusCode = str(responce2.status_code)

if '20' in statusCode:
    print("Success!")
    print ('Error Code: ' + statusCode)
elif '40' in statusCode:
    print ("Somethings Wrongs on this Side!")
    print ('Error Code: ' + statusCode)
elif '50' in statusCode:
    print ("Server Side Error (will be 501 if no openflow nodes are connected to the controller)")
    print ('Error Code: ' + statusCode)
