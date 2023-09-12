# MSIS-5193-Assignments
"""
MSIS 5193 Assignment 1 README

Description:
------------
This Python script performs several data analysis tasks using Pandas, focusing on a dataset about flights.
The script includes the following functionalities:
1. Imports a CSV file and generates a summary of the DataFrame.
2. Performs data aggregation, filtering, and sorting operations to answer specific questions.

Requirements:
-------------
Software and Libraries:
- Python 3.x
- Pandas library

To install Pandas, run the following command:
# pip install pandas

Data File:
- CSV file located at `/Users/brocktbennett/GitHub/Data/flights.csv`

How to Run:
-----------
1. Make sure you have Python 3.x installed.
2. Install the Pandas library.
3. Place your data file `flights.csv` in the path specified in the script or update the script with the correct file path.

To execute the script, run the following command in your terminal:
# python your_script_name.py

Code Overview:
--------------
Import Libraries:
# import pandas as pd
# import datetime

Main Function (`main()`):
The `main()` function encapsulates all the code functionalities.

- Display Current Time: Displays the current time when the code is run.
- Assignment Details: Prints assignment details such as due date and author name.

Task 1: Import Files and Generate Summary:
- Imports a CSV file located at a specific path.
- Prints basic DataFrame information such as the number of rows and columns.
- Prints the data types of each column.

  Task 1.1: DataFrame Summary:
  - Reads the CSV file into a DataFrame and displays its shape and data types.

  Task 1.2: Specific Information:
  1. Counts the number of unique carriers.
  2. Counts the size of each carrier in terms of the number of flights.

Task 2: Data Aggregation, Filtering, and Sorting:
  Task 2.1: Mean Delays for Each Flight:
  - Groups data by carrier and flight, then calculates and sorts mean departure and arrival delays.

  Task 2.2: Average Delays in Winter vs. Summer:
  - Compares the average arrival delays in winter and summer months.

Author:
-------
- Brock Bennett
"""

# Your original code starts here.
# MSIS 5193 Assignment 1
# Due Date: Sept 13th (11:59pm)
# Author: Brock Bennett
# Date: Sep 5, 2023