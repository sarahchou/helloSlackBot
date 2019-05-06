import requests
import json

url = "https://slack.com/api/chat.postMessage"

payload = "{'channel': \"CJ9S864SG\", 'text': \"testing the test.py script\"}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer xoxp-624597919830-616113532641-616119678305-7f2a93f2e1272a28f451e11fe2b9ac12",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(json.dumps(response.json(), sort_keys=True, indent=4))