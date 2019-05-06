import requests
import json

url = "https://slack.com/api/chat.postMessage"

payload = "{'channel': \"CJ9S864SG\", 'text': \"testing the test.py script\"}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer xxxxxxx",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(json.dumps(response.json(), sort_keys=True, indent=4))