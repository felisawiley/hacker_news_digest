#Handle the email-related tasks.

import requests
from emailer import send_email
from config import url


def fetch_snapshot(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching snapshot: {e}")
        return None
    

def fetch_story(story_id):
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    try:
        response = requests.get(story_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching story with ID {story_id}: {e}")
        return None
    

def job():
    snapshot = fetch_snapshot(url)
    #print(f"Fetched snapshot: {snapshot}")
    if snapshot is not None:
        jobs = []
        for job_id in snapshot:
            job = fetch_story(job_id)
            if job is not None:
                jobs.append(job)
        #print(f"Job stories: {jobs}")
        print("calling send email...")
        send_email(jobs, url)
    else:
        print("Failed to fetch snapshot. Skipping email sending.")

print("hacker news email digest scraper.py complete")
