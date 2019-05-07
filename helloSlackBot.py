import requests
import json
import time
import datetime
import os

# Initializing Variables
headers = {}
data = {}
uri = 'https://slack.com/api/chat.scheduleMessage'
channel = 'CJ9S864SG'
slack_token = os.environ['SLACK_BOT_TOKEN']

# Put in variables for the scheduled time to be posted at here: 
sched_year = 2019
sched_month = 5
sched_day = 7
sched_hour = 11
sched_minute = 9

# For some reason, the hour is 4 hours ahead. i.e. to schedule at 9am, have to make it 13...
sched_time = (datetime.datetime(sched_year,sched_month,sched_day,sched_hour + 4,sched_minute) - datetime.datetime(1970,1,1)).total_seconds()

# Put message content you want here:
message = "Message scheduled for " + str(sched_hour) + ":" + str(sched_minute)

# Fill in headers and data dictionaries
headers.update({'Content-Type': 'application/json'})
headers.update({'Authorization': 'Bearer ' + slack_token})

data.update({'channel': channel})
data.update({'text': message})
data.update({'post_at': sched_time})

data_json = json.dumps(data)

# Make the request
r = requests.post(uri, headers=headers, data=data_json)

# For testing purposes, print the json output of the request: 
print(json.dumps(r.json(), sort_keys=True, indent=4))
