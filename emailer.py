#use this module to construct the email format

import smtplib #used for sending emails using the SMTP (Simple Mail Transfer Protocol)
from email.mime.text import MIMEText #allows us to construct the email message in a specific format (HTML)
from config import sender, recipient, password, url
import datetime

#get today's date
date = datetime.date.today()

#define a function for sending the email
def send_email(job_stories, url):
    subject = f"Hacker News Job Digest for {date}"

    #begin constructing email
    html_content = "<ul>"
    
    #loop through each job posting
    for job in job_stories:
        title = job["title"]
        job_url = job.get("url") 

        #check if job url exists
        if job_url:
            #if job url does exist, append a list item with a hyperlink to the job posting
            html_content += f'<li><a href="{job_url}">{title}</a></li>'
        else:
            #if job url does not exist, just list the job title
            html_content += f'<li>{title}</li>'
    html_content += "</ul>"

    #construct a MIMEText email object (MIME = Multipurpose Internet Mail Extensions)
    msg = MIMEText(html_content, "html") #specify the type of content the email will hold
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    
    #define the server and port -- 465 is the standard SMTP SSL port
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    print("Attempting to send email")

    #create a secure SMTP connection, authenticate user credentials, and send the email
    with smtplib.SMTP_SSL(smtp_server,smtp_port) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())

        print(f"Email sent successfully on {date}")

print("hacker news email digest emailer.py complete")
