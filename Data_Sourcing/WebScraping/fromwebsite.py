import pandas as pd
from bs4 import BeautifulSoup
import requests

# Getting all data-related jobs in India
theweb = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=data&txtLocation=india').text
soup = BeautifulSoup(theweb, 'lxml')

jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

# Initialize lists to store job details
job_titles = []
published_dates = []
skills_required = []

for job in jobs:
    job_title = job.find('header', class_="clearfix").text.strip()
    skills = job.find('span', class_='srp-skills').text.strip()

    try:
        published_date = job.find('span', class_='sim_posted').span.text
        if 'few' in published_date:
            continue
    except AttributeError:
        published_date = "N/A"

    if 'few' not in published_date:
        job_titles.append(job_title)
        published_dates.append(published_date)
        skills_required.append(skills)

# Create a pandas dataframe
data = {
    'Job Title': job_titles,
    'Published Date': published_dates,
    'Skills Required': skills_required
}
df = pd.DataFrame(data)

# Save the dataframe as a CSV file
df.to_csv('job_listings.csv', index=False)

print("Job listings saved to job_listings.csv")