# MSIS 5193 Assignment 2
# Due Date: Sept 20th (11:59pm)
# Author: [Your Name]
# Date: [Current Date]

# Importing necessary libraries
import pandas as pd
import datetime


# Main function where all operations will be performed
def main():
    # Get and display the current time when code is running
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Code is running at: {current_time}\n")

    # Print assignment details
    print("The start of my assignment\n"
          "MSIS 5193 Assignment 2\n"
          "Due date: Sept 20th (11:59pm) CST\n"
          "Author: [Brock T. Bennett]\n")

    # --- Task 1: Data Preprocessing (Total 55 points) ---
    print("Task 1: Data Preprocessing")
    print("---------------------------------------------------------------")

    # Task 1.1: Load the dataset and handle missing values (5 points)
    # Load the '2017CHR_CSV_Analytic_Data-new.csv' file into a DataFrame.
    # Check for missing values in the DataFrame and handle them as needed.
    # Display the result indicating which columns had missing values.

    # Task 1.2: Remove identifier columns (5 points)
    # Drop columns: '5-Digit FIPS Code', 'statecode', 'countycode', 'county'.

    # Task 1.3: Z-score normalization (5 points)
    # Normalize columns: ['Poor physical health days Value', 'Poor mental health days Value', 'Food environment index Value'].

    # Task 1.4: Create 'Diabetes-level' column (20 points)
    # Categorize 'Diabetes Value' into four groups (low, median low, median high, high).
    # Store the results in the new 'Diabetes-level' column.

    # Task 1.5: Feature selection (20 points) (optional)
    # Split the DataFrame into features (X) and the target variable ('Diabetes-level') (y).
    # Use feature selection techniques to find the top 5 relevant features for 'Diabetes-level'.

    # --- Task 2: Output Screenshots (Total 5 points) ---
    print("Task 2: Output Screenshots")
    print("---------------------------------------------------------------")

    # Capture screenshots of the output for each sub-task in Task 1.
    # Save the screenshots in a Word file as required by the assignment.


# Execute the main function when the script is run
if __name__ == "__main__":
    main()
