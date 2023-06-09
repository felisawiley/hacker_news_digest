# hacker_news_digest

This Python project sends an email digest containing a snapshot of the HN Hiring webpage for Python jobs every Friday at 8:00 am. The email provides an overview of the page's primary content, and when you click the link in the email, it takes you directly to the website.

### Dependencies

The project depends on the following Python libraries:
- requests
- beautifulsoup4
- schedule


### Installation

Clone the repository or download the project as a zip file and extract it to your desired location.

Navigate to the project folder in your terminal or command prompt and run the following command to install the required libraries:

Copy code:
- pip install -r requirements.txt
- OR pip3 install -r requirements.txt
Update the config.py file with your Gmail address and password or app-specific password.


### Usage

To start the email digest service, run the following command in your terminal or command prompt:

Copy code:
- python scheduler.py
- OR python3 scheduler.py
The script will continue running and send the email digest every Friday at 8:00 am.


### Project Structure 

The project is organized into the following files and folders:

- config.py: Stores the email configurations and other constants/settings.
- scraper.py: Handles the web scraping tasks.
- emailer.py: Handles email-related tasks.
- scheduler.py: Schedules and runs the tasks.
- requirements.txt: List the required packages for the project.


### Security Notice

Storing your email credentials in plain text in a script is not secure. You should use a more secure method in a production environment, like environment variables or a secrets manager.

Also, note that the Gmail account you use for sending emails should have "Less secure apps" enabled, or you should use an app-specific password. Be aware that enabling "Less secure apps" may pose security risks.
