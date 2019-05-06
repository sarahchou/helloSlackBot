import time
import datetime

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
sched_minute = 5

print("local time: " + str(local_time))

print("Scheduled time: " + str((datetime.datetime(sched_year,sched_month,sched_day,sched_hour,sched_minute) - datetime.datetime(1970,1,1)).total_seconds()))

print("Current time: " + str((datetime.datetime(cur_year,cur_month,cur_day,cur_hour,cur_minute) - datetime.datetime(1970,1,1)).total_seconds()))
