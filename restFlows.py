import requests
import json

##Add Try catch for this whole boiiiii

payload = {'input':{'NodeID':'openflow:66160483351808'}}

flowResponse = requests.get("http://10.43.8.11:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:66160483351808/table/0/", auth=('admin','admin'))

print("GET nodes: " + str(flowResponse.status_code))

fuckingjson = flowResponse.json()
print(fuckingjson)

# for x in fuckingjson['nodes']['node']:
#    print(x['id'])



