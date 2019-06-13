import json
jsonfile=open("jsondump1.json","a")
data={"name":"bharath","mobile":"8756897567","gmail":"bharath@gmail.com"}
json.dump(data,jsonfile)
jsonfile.close()