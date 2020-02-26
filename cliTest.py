import sys
from ctypes import *
import requests
import json

flowgen = cdll.LoadLibrary("./buildflow.so")

class go_string(Structure):
    _fields_ = [
        ("p", c_char_p),
        ("n", c_int)]

print("""
  ________  ________   _____  ___        _______  __      _______    _______  __   __  ___       __      ___      ___       
 /"       )|"      "\ (\"   \|"  \      /"     "||" \    /"      \  /"     "||"  |/  \|  "|     /""\    |"  |    |"  |      
(:   \___/ (.  ___  :)|.\\   \    |    (: ______)||  |  |:        |(: ______)|'  /    \:  |    /    \   ||  |    ||  |      
 \___  \   |: \   ) |||: \.   \\  |     \/    |  |:  |  |_____/   ) \/    |  |: /'        |   /' /\  \  |:  |    |:  |      
  __/  \\  (| (___\ |||.  \    \. |     // ___)  |.  |   //      /  // ___)_  \//  /\'    |  //  __'  \  \  |___  \  |___   
 /" \   :) |:       :)|    \    \ |    (:  (     /\  |\ |:  __   \ (:      "| /   /  \\   | /   /  \\  \( \_|:  \( \_|:  \  
(_______/  (________/  \___|\____\)     \__/    (__\_|_)|__|  \___) \_______)|___/    \___|(___/    \___)\_______)\_______)     
""")

print("Alpha 0.6.9\n")

print("1 - Create Rule\n2 - Switch Node Managment \nQ - Quit")

nums = 0


loop=1
innerLoop1=1
innerloop2=1
while loop:
    selec = input(">>> ")
    print(selec)
    if selec=='1':
        print("~~~ Flow Creation Menu ~~~\n1 - New Flow\n2 - Show Current Flow\n3 - Send Flow")
        while innerLoop1: 
            selec2 = input(">>> ")
            if selec2=='1':
                print("\nAdd rule based on.... ")
                inputSrcIP =  input(">>> SRC IP: ")
                inputDstIP =  input(">>> DST IP: ")
                srcIP = inputSrcIP + '/32'
                dstIP = inputDstIP + '/32'
                portType = input(">>> 'UDP' / 'TCP': ")
                srcTcp = input(">>> SRC PORT: ")
                dstTcp = input(">>> DST PORT: ")
            elif selec2=='2':
                print("\nThe current flow will deliver the following rules:\n")
                print("Block Traffic Based on\nIP SRC: " + srcIP)
                print("IP DST: " + dstIP)
                print("Type: " + portType)
                print("Port SRC: " + srcTcp)
                print("Port DST: " + dstTcp)                            
            elif selec2=='3':
                Src = srcIP.encode('utf-8')
                Dst = dstIP.encode('utf-8')
                sP = srcTcp.encode('utf-8')
                dP = dstTcp.encode('utf-8')
                SSr = go_string(c_char_p(Src), len(Src))
                DDs = go_string(c_char_p(Dst), len(Dst))
                SSp  = go_string(c_char_p(sP), len(sP))
                DDp  = go_string(c_char_p(dP), len(dP))
                #print the entered values to confirm xml being created with that input
                #print(Src)
                #print(SSr)
                #print(Dst)
                #print(DDs)
                #print(sP)
                #print(SSp)
                #print(dP)
                #print(DDp)
        
                flowgen.Goflowgo(SSr,DDs,SSp,DDp)             
                xmlfile = "flow.xml"
                print("xml create")
                headers = {'content-type': 'application/xml'}
                with open(xmlfile) as xml:
                    responce2 = requests.post("http://10.43.8.11:8181/restconf/operations/sal-flow:add-flow",data=xml,headers=headers,auth=('admin','admin'))
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
    elif selec=='2':
        print("Switch Node Managment")
        print("1 - List Each Node\n 2 - Display Active Rules\n 3- Delete Rules From Node")
        while innerloop2==1:
            selec3 = input(">>> ")
    else:
        print("Not an option")
    

                


