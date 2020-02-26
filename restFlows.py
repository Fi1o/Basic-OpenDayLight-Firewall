import requests
import json

##Add Try catch for this whole boiiiii

payload = {'input':{'NodeID':'openflow:1'}}

flowResponse = requests.get("http://10.43.8.11:8181/restconf/operational/opendaylight-inventory:nodes/", auth=('admin','admin'))

print("GET nodes: " + str(flowResponse.status_code))

fuckingjson = flowResponse.json()
print(fuckingjson)



for x in fuckingjson:
    print(x)
    # if x['id'] in 'openflow:1':
     #   for y in x['flow-node-inventory:table']:
       #  if y['id'] == 0:
        #    for z in y['flow']:
         #       print(z['id'])
          #      print(z['instructions'])


# Ideas
# for x in json (figure our the values that the flows can take in the table)  
#    print the id of an active node
#        if that ID is in the flow database? or where ever they are stored
#            printing the entire flow or that id