import requests
import json

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