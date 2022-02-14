import json
import requests

login = requests.post('https://cplab:4434/web_api/v1.5/login', json={'user': 'admin', 'password': 'pass1234'}, verify="rootca.cer")

#store session ID
#print("\n-----------------SID'i buldum-------------------------: ",login.json()["sid"] + "\n")

#pull rulebase
response = requests.post('https://cplab:4434/web_api/v1.5/show-access-rulebase', json={'name' : 'Network'}, headers={'X-chkp-sid': login.json()["sid"]}, verify="rootca.cer")

#check rulebase
for p in range(len(response.json()["rulebase"])):
#check inline layers
    if "inline-layer" in response.json()["rulebase"][p]:
        ruleuid = response.json()["rulebase"][p]["inline-layer"]
#        print("\n-----------------------RuleUID: ", ruleuid, "----------------------------------\n")
#check sub-rules
        inlinerule = requests.post('https://cplab:4434/web_api/v1.5/show-access-rulebase', json={'uid' : ruleuid}, headers={'X-chkp-sid': login.json()["sid"]}, verify="rootca.cer")
        for px in range(len(inlinerule.json()["rulebase"])):
            if inlinerule.json()["rulebase"][px]["enabled"] == False:
                print("Su kural disabled: ",p,".",inlinerule.json()["rulebase"][px]["rule-number"], "----------------------------------")
#check ordered rules
    elif response.json()["rulebase"][p]["enabled"] == False:
        print("Su kural disabled: ", response.json()["rulebase"][p]["rule-number"], "----------------------------------")