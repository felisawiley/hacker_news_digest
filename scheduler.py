#this module schedules the job function from scraper.py to run the task at a specific date and time every week

import sched
import time
from scraper import job

def schedule_and_run():
    scheduler = sched.scheduler(time.time, time.sleep) #returns the current time in seconds and time.sleep is used to delay execution
    scheduler.enterabs(time.time(), 1, job) #schedules the job function to be run as soon as possible, 1 is the priority
    while True: #begin inifinity loop
        now = time.localtime()
        #if the current day of the week if Friday (4), and the hour is 8:00 am, run job()
        if now.tm_wday == 4 and now.tm_hour == 8 and now.tm_min == 0:
            job()
        #pauses the execution of the loop for 60s before checking the time again
        time.sleep(60) 


#used to run the script directly 
if __name__ == "__main__":
    schedule_and_run()
print("hacker news email digest scheduler.py complete")
