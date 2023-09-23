import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

# MSIS 5193 Assignment 2
# Due Date: Sept 20th (11:59pm)
# Author: Brock Bennett
# Date: Sep 10th, 2023

# Load the CSV file into a DataFrame
print("Load the CSV file into the dataframe 'analytics_data_df'")
print("Loading the CSV file...")
file_path = "/Users/brocktbennett/GitHub/Project Data/2017CHR_CSV_Analytic_Data-new.csv"
analytics_data_df = pd.read_csv(file_path)
print("CSV file loaded successfully.\n")

# Print number of columns and rows in the DataFrame
print("Print number of columns and rows in the DataFrame:")
print(f"Number of Columns before drop: {analytics_data_df.shape[1]}")
print(f"Number of Rows before drop: {analytics_data_df.shape[0]}\n")
initial_num_columns = analytics_data_df.shape[1]
initial_num_rows = analytics_data_df.shape[0]

# # Display data types of each column
# print("Display data types of each column:\n---------------------------------")
# print("Data Types of Each Column:")
# print(analytics_data_df.dtypes)
# print()

# Display the top 10 rows of the DataFrame
print("Display the top 10 rows of the DataFrame")
print("Top 10 Rows of DataFrame:\n---------------------------------------------")
print(analytics_data_df.head(10))
print()

# Task 1.1: Check for missing values and impute if necessary
print("Task 1.1: Checking for missing values and impute if necessary...")
missing_columns = analytics_data_df.columns[analytics_data_df.isnull().any()]

if not missing_columns.empty:
    print("Columns with missing values have been identified:")
    for col in missing_columns:
        # Calculate the imputed value (in this case, the mean)
        imputed_value = analytics_data_df[col].mean()
        # Format imputed value to three decimal places
        imputed_value = round(imputed_value, 3)

        # Impute missing values
        analytics_data_df[col].fillna(imputed_value, inplace=True)

        print(f"Imputed missing values in column '{col}' with value: {imputed_value}")

    print("Missing values imputed.")
else:
    print("No missing values were detected, so the DataFrame remains unchanged. However, I have included a function "
          "to handle missing data if it is found.")
print("End of Task 1.1\n")

# Task 1.2: Remove the identifier columns
print("Task 1.2: Remove the identifier columns - 5-Digit FIPS Code, statecode, countycode, county.")
# Define columns to drop
columns_to_drop = ["5-Digit FIPS Code", "statecode", "countycode", "county"]



# Capture the dropped column names before dropping
dropped_columns = analytics_data_df[columns_to_drop].columns.tolist()

# Drop columns with inplace=True
analytics_data_df.drop(columns=columns_to_drop, inplace=True)

# Print number of columns and rows in DataFrame
print(f"Number of Columns before drop '{initial_num_columns}' after drop: '{analytics_data_df.shape[1]}'")
print(f"Number of Rows before drop '{initial_num_rows}' after drop: '{analytics_data_df.shape[0]}'")
columns_dropped = initial_num_columns - analytics_data_df.shape[1]
rows_dropped = initial_num_rows - analytics_data_df.shape[0]

# Check if any columns were dropped
if dropped_columns:
    print(f"{columns_dropped} Columns and {rows_dropped} Rows were dropped.")
    print("Columns dropped:", ", ".join(dropped_columns))
    print("End of Task 1.2\n")
else:
    print("No Columns were dropped")

# Task 1.3: Use z-score normalization
print("Task 1.3: Use z-score normalization to normalize selected columns...")
columns_to_normalize = ["Poor physical health days Value", "Poor mental health days Value",
                        "Food environment index Value"]

# Check for missing values in the selected columns
missing_values = analytics_data_df[columns_to_normalize].isnull().sum()

# Print the number of missing values for each column
for column, count in missing_values.items():
    print(f"Missing values in '{column}': {count}")

# Perform z-score normalization
scaler = preprocessing.StandardScaler()

# Fit and transform the selected columns using z-score normalization
analytics_data_df[columns_to_normalize] = scaler.fit_transform(analytics_data_df[columns_to_normalize])

normalized_df = pd.DataFrame(analytics_data_df, columns=columns_to_normalize)

# Print the z-score normalized values
print("z-score Normalized values: ")
print(normalized_df)

# Task 1.4: Create a new column Diabetes-level by coding Diabetes Value into four groups and label them
# low, median low, median high, and high

# Manually set bin edges based on the given information
bins = [0.033000, 0.095000, 0.111000, 0.128000, float('inf')]

# Create labels for the bins
labels = ['low', 'median low', 'median high', 'high']

# Create a new column "Diabetes-level" with custom ranges
analytics_data_df['Diabetes-level'] = pd.cut(analytics_data_df['Diabetes Value'], bins=bins, labels=labels, include_lowest=True)

# Print out the Diabetes Values to determine labels
print(analytics_data_df['Diabetes Value'].describe())

# Print the updated DataFrame with ranges
print("\nRanges: ")
for category in labels:
    category_values = analytics_data_df[analytics_data_df['Diabetes-level'] == category]['Diabetes Value']
    min_cat_value = category_values.min()
    max_cat_value = category_values.max()
    print(f"{category}: {min_cat_value:.3f} - {max_cat_value:.3f}")

print("\nUpdated DataFrame")
print(analytics_data_df[['Diabetes Value', 'Diabetes-level']])

print("Preview of DataFrame with relevant columns:")
print(analytics_data_df[['Diabetes Value', 'Diabetes-level']].head())



# Task 1.5: Apply Feature selection to find the top 5 relevant features
print("Task 1.5: Apply Feature selection to find the top 5 relevant features...")



# Define target column and input columns
target_column = analytics_data_df['Diabetes-level']

# print("This is the columns of the dataframe")
# print(analytics_data_df.columns)

# Create a list of columns to use as input features (all columns except 'Diabetes Value' and 'Diabetes-level')
input_columns = [col for col in analytics_data_df.columns if col not in ['Diabetes Value', 'Diabetes-level']]

# Split the data into X (input) and y (target)
X = analytics_data_df[input_columns]
y = analytics_data_df[target_column]

# # Describe column Diabetes Level
# print("Printing out Describing Column")
# print(analytics_data_df['Diabetes Value'].describe())

# Apply feature scaling to make sure all input features are non-negative
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Apply feature selection using chi-squared test to the scaled data
selector = SelectKBest(score_func=chi2, k=5)  # Select the top 5 features
X_new = selector.fit_transform(X_scaled, y)

# Store the result of selector.get_support() in a variable
support = selector.get_support()

# Get the names of the selected features
selected_features = [input_columns[i] for i, is_selected in enumerate(support) if is_selected]

# Print the names of the top 5 relevant features
print("Top 5 Relevant Features to", target_column)
print(selected_features)
print()


