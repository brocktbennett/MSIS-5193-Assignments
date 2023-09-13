# MSIS 5193 Assignment 1
# Due Date: Sept 13th (11:59pm)
# Author: Brock Bennett
# Date: Sep 5, 2023

# Importing necessary libraries
import pandas as pd
import datetime


#Changed made and finished on Sep 12, 2023
# Main function where all operations will be performed
def main():
    # Get and display the current time when code is running
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Code is running at: {current_time}\n")

    # Print assignment details
    print("The start of my assignment\n"
          "MSIS 5193 Assignment 1\n"
          "Due date: Sept 13th (11:59pm) CST\n"
          "Author: Brock Bennett\n")

    # --- Task 1: Import Files and Generate Summary (Total 15 points) ---
    print("Task 1: Import files and generate some summary.")
    print("---------------------------------------------------------------")

    # Task 1.1: Import CSV file into DataFrame and display basic DataFrame information (5 points)
    # Define file path
    file_path = "/Users/brocktbennett/GitHub/Project Data/flights.csv"
    # Read CSV file into DataFrame
    flight_df = pd.read_csv(file_path)

    # Print number of columns and rows in DataFrame
    print(f"Number of Columns: {flight_df.shape[1]}")
    print(f"Number of Rows: {flight_df.shape[0]}")
    # Display data types of each column
    print("Data Types of Each Column:")
    print(flight_df.dtypes)
    print()

    # Task 1.2: Show specific information using Pandas functionalities (10 points)
    # 1.2a: Count unique carriers (5 points)
    unique_carriers = flight_df['carrier'].nunique()
    # Display number of unique carriers
    print(f"How many carriers exist?: {unique_carriers}")
    # 1.2b: Count and display the size of each carrier in terms of number of flights (5 points)
    size_of_each_carrier = flight_df['carrier'].value_counts()
    print("What is the size of each carrier in terms of the number of flights?")
    print(size_of_each_carrier)
    print()

    # --- Task 2: Data Aggregation, Filtering, and Sorting (Total 20 points) ---
    print("Task 2: Data aggregation, filtering, and sorting.")
    print("---------------------------------------------------------------")

    # Task 2.1: Calculate and sort mean delays for each flight (10 points)
    # Group by carrier and flight and calculate mean delays
    mean_delays = flight_df.groupby(['carrier', 'flight'])[['dep_delay', 'arr_delay']].mean()
    # Sort the resulting DataFrame
    mean_delays_sorted = mean_delays.sort_values(by=['dep_delay', 'arr_delay'], ascending=False)
    # Display sorted mean delays
    print("Mean Dep_Delay and Arr_Delay for Each Flight, Sorted in Descending Order:")
    print(mean_delays_sorted)
    print()

    # Task 2.2: Compare average delays in winter and summer (10 points)
    # Filter data for winter months (January, February)
    winter_months = flight_df[flight_df['month'].isin([1, 2])]
    # Filter data for summer months (June, July)
    summer_months = flight_df[flight_df['month'].isin([6, 7])]
    # Calculate and display average delays for winter and summer
    winter_avg_delay = winter_months['arr_delay'].mean()
    summer_avg_delay = summer_months['arr_delay'].mean()
    print()

    print("Compare the Average Arr_Delay in Winter vs Summer:")
    print(f"Average Arrival Delay in January and February: {winter_avg_delay}")
    print(f"Average Arrival Delay in June and July: {summer_avg_delay}")
    print()
    print("Checking to see which season has more average delays...")

    # Display which season has more average delays
    if winter_avg_delay > summer_avg_delay:
        print("Answer: Winter months (January and February) have higher average arrival delays.")
    elif winter_avg_delay < summer_avg_delay:
        print("Answer: Summer months (June and July) have higher average arrival delays.")
    else:
        print("Answer: Winter and Summer months have the same average arrival delays.")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
