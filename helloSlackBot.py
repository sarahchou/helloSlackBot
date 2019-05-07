import requests
import json
import time
import datetime

headers = {}
data = {}
uri = 'https://slack.com/api/chat.scheduleMessage'

sched_year = 2019
sched_month = 5
sched_day = 7
sched_hour = 9
sched_minute = 40

channel = 'CJ9S864SG'

#for some reason, the hour is 4 hours ahead. To schedule at 9am, have to make it 13...
sched_time = (datetime.datetime(sched_year,sched_month,sched_day,sched_hour + 4,sched_minute) - datetime.datetime(1970,1,1)).total_seconds()

postTime = sched_time
message = "Message scheduled for " + str(sched_hour) + ":" + str(sched_minute)

headers.update({'Content-Type': 'application/json'})
headers.update({'Authorization': 'Bearer XXXXXXXXXXX'})

data.update({'channel': channel})
data.update({'text': message})
data.update({'post_at': postTime})

data_json = json.dumps(data)

r = requests.post(uri, headers=headers, data=data_json)

print(json.dumps(r.json(), sort_keys=True, indent=4))

print(time.localtime)