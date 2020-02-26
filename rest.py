import requests
import json

##Add Try catch for this whole boiiiii


payload = {'input':{'NodeID':'openflow:1'}}

responce2 = requests.get("http://10.43.8.11:8181/restconf/operational/opendaylight-inventory:nodes/",auth=('admin','admin'))

print("GET nodes: " + str(responce2.status_code))

fuckingjson = responce2.json()
print(fuckingjson)
for x in fuckingjson['nodes']['node']:
    print(x['id'])
    if x['id'] in 'openflow:1':
        for y in x['flow-node-inventory:table']:
         if y['id'] == 0:
            for z in y['flow']:
                print(z['id'])
               # print(z['instructions'])



