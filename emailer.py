#Handle the web scraping tasks.

import smtplib
from email.mime.text import MIMEText
from config import sender, recipient, password



def send_email(job_stories, url):
    subject = "Hacker News Job Digest"
    html_content = "<ul>"
    for job in job_stories:
        title = job["title"]
        job_url = job.get("url") 
        if job_url:  # Add this line to check if the job_url is not None
            html_content += f'<li><a href="{job_url}">{title}</a></li>'
        else:
            html_content += f'<li>{title}</li>'
    html_content += "</ul>"

    msg = MIMEText(html_content, "html")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    print("Attempting to send email")

    with smtplib.SMTP_SSL(smtp_server,smtp_port) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())

        print("Email sent successfully")

print("hacker news email digest emailer.py complete")
