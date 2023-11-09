# MSIS 5193 Assignment 7
# Due Date: Nov 8th (11:59pm – nighttime)
# Author: Brock Bennett
# Date: Oct 31, 2023

# Importing necessary libraries for web scraping
import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Get the webpage content
url = "https://dbworld.sigmod.org/browse.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Task 1: Get the title of the webpage
title = soup.title
title_string = soup.title.string
print("Task 1: Title of the webpage:", title)
# print(title_string)

# Task 2: Get the list of tags on the webpage
tags = [tag.name for tag in soup.find_all()]
print("Task 2: List of tags on the webpage:")

# Task 3: Get the number of Oct in the web page.
# Find all occurrences of 'Oct' in the parsed HTML and count them
october_count = 0
for tag in soup.find_all(text=True):
    if 'Oct' in tag:
        october_count += tag.count('Oct')

# Print the count of occurrences
print("Number of 'Oct' occurrences:", october_count)


# Find all <p> tags in the HTML
for tag in soup.find_all('p'):
    # Get the text content of the <p> tag
    line = tag.text

    # Check if 'Oct' is present in the text
    if 'Oct' in line:
        # Split the text using 'Oct' as a delimiter and keep the first part (before 'Oct')
        oct_part = line.split('Oct', 1)[0]
        print('Oct:', oct_part.strip())  # Print the stripped 'Oct' part

# Task 4: Find all the URLs in the href attribute of tag 'a' and save to a CSV file
urls = [a['href'] for a in soup.find_all('a', href=True)]
with open('urls.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["URLs"])
    for url in urls:
        writer.writerow([url])

print("Task 4: URLs saved to 'urls.csv'")
