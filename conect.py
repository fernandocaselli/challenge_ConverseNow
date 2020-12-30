import requests
import json

url = "http://127.0.0.1:5000/"
data={"accent": "mexicano"}

myResponse = requests.get(url, params=data, verify=True)
print (myResponse.status_code)

if(myResponse.ok):

    jData = json.loads(myResponse.content)

    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
        print(key + " : " + str(jData[key]))
else:
    myResponse.raise_for_status()