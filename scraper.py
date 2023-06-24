#this modules fetches the necessary data from the Hacker News API, processes it, and then sends the email using the functionality defined in the other modules

import requests #used for making HTTP requests 
from emailer import send_email
from config import url

#the following functions are required to obtain the job postings from HN - they collect and process the data 
#fetches a snapshot from the Hacker News API with the latest story IDs
def fetch_snapshot(url):
    #attempts to get a response from the URL and parse it as JSON (needs to parse as JSON because data retrieved from HN API is in JSON)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json() #converts from JSON to a list -- easier to work with in Python
    #handles any potential exceptions
    except requests.exceptions.RequestException as e:
        print(f"Error fetching snapshot: {e}")
        return None
    
#fetches a specific job positing using its ID, constructs the URL for the specific job posting and sends a GET request to the URL (to retrieve the data -- a type of HTTP)
def fetch_story(story_id):
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    try:
        response = requests.get(story_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching story with ID {story_id}: {e}")
        return None
    
#fetches a snapshot of job postings, iterates over the IDs to capture details of each job, appends to a list
def job():
    snapshot = fetch_snapshot(url)
    if snapshot is not None:
        jobs = []
        for job_id in snapshot:
            job = fetch_story(job_id)
            if job is not None:
                jobs.append(job)
        print("calling send email...")
        #calls send email using predefined functionality/ formatting
        send_email(jobs, url)
    else:
        print("Failed to fetch snapshot. Skipping email sending.")

print("hacker news email digest scraper.py complete")
