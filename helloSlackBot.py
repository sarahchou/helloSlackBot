import requests
import json
import time
import datetime

headers = {}
data = {}
uri = 'https://slack.com/api/chat.scheduleMessage'

local_time = time.localtime()
cur_year = local_time.tm_year
cur_month = local_time.tm_mon
cur_day = local_time.tm_mday
cur_hour = local_time.tm_hour
cur_minute = local_time.tm_min


sched_year = 2019
sched_month = 5
sched_day = 6
sched_hour = 10
sched_minute = 50

channel = 'CJ9S864SG'
postTime = 1557222600.0
#postTime = str((datetime.datetime(sched_year,sched_month,sched_day,sched_hour,sched_minute) - datetime.datetime(1970,1,1)).total_seconds())
#postTime = str((datetime.datetime(cur_year,cur_month,cur_day,cur_hour,cur_minute) - datetime.datetime(1970,1,1)).total_seconds())
message = 'The time is '


headers.update({'Content-Type': 'application/json'})
headers.update({'Authorization': 'Bearer xxxxxxxxxxxxxx'})

data.update({'channel': channel})
data.update({'text': message})
data.update({'post_at': postTime})

data_json = json.dumps(data)

r = requests.post(uri, headers=headers, data=data_json)

print(json.dumps(r.json(), sort_keys=True, indent=4))

print(time.localtime)