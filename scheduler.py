#Schedule and run the tasks.

import schedule
import time
from emailer import send_email
from scraper import job
from config import url


schedule.every().friday.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)


print("hacker news email digest scheduler.py complete")
