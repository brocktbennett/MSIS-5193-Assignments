# MSIS 5193 Assignment 5
# Due Date: Oct 18th (11:59pm)
# Author: Brock Bennett
# Date: Oct 9, 2023

# Importing necessary libraries
import re  # needed for regular expressions in Task 3
from fpdf import FPDF

# Load the .txt file into the dataframe 'mbox'
file_path = "/Users/brocktbennett/GitHub/Project Data/Data Science Programming Data/mbox.txt"
with open(file_path, 'r') as file:
    lines = file.readlines()  # Using readlines to get list of lines

print("MSIS 5193")
print("Assignment 5 – Due Oct 18th (11:59pm)")
print("Use the mbox.txt file to finish the following tasks:")

# Task 1: Count the total number of lines with content
lines_with_content = [line for line in lines if line.strip()]  # Filtering out empty or whitespace-only lines
print("\nTask 1: Total number of lines with content:", len(lines_with_content))

# Task 2: Get the lines with “X-DSPAM-Confidence:”
xdspam_lines = [line for line in lines if "X-DSPAM-Confidence:" in line]
print("\nTask 2: Lines with 'X-DSPAM-Confidence:'")
for line in xdspam_lines:
    print(line.strip())  # Stripping to avoid extra newlines
print("\nNumber of 'X-DSPAM-Confidence: ' lines found: ", len(xdspam_lines))

# Task 3: Use Regex to get all the URLs starting with “http:\\”
pattern = r"http://[^\s]+"  # Matches 'http://' followed by any non-whitespace characters
urls = re.findall(pattern, ''.join(lines))  # Joining lines back to single string
print("\nTask 3: URLs starting with 'http://':")
for url in urls:
    print(url)
print("\nNumber of URLs starting with 'http://':", len(urls))
