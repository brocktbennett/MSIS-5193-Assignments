# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif

# Load the CSV file into a DataFrame
df = pd.read_csv("datasets/2017CHR_CSV_Analytic_Data-new.csv")

# Task 1: Check for missing values and impute if necessary
missing_columns = df.columns[df.isnull().any()]
if not missing_columns.empty:
    for col in missing_columns:
        # Impute missing values (you can choose a method, e.g., mean, median, or custom)
        df[col].fillna(df[col].mean(), inplace=True)
    print("Missing values imputed.")
else:
    print("No missing values found. DataFrame remains as is.")

# Task 2: Drop identifier columns
df.drop(columns=["5-Digit FIPS Code", "statecode", "countycode", "county"], inplace=True)
print("Identifier columns dropped.")

# Task 3: Z-score normalization
columns_to_normalize = ["Poor physical health days Value", "Poor mental health days Value", "Food environment index Value"]
scaler = StandardScaler()
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])
print("Columns normalized using Z-score.")

# Task 4: Create "Diabetes-level" column
def categorize_diabetes(value):
    if value < threshold_low:
        return "low"
    elif threshold_low <= value < threshold_median_low:
        return "median low"
    elif threshold_median_low <= value < threshold_median_high:
        return "median high"
    else:
        return "high"

# Define thresholds for categorization
threshold_low = df["Diabetes Value"].quantile(0.25)
threshold_median_low = df["Diabetes Value"].quantile(0.5)
threshold_median_high = df["Diabetes Value"].quantile(0.75)

# Apply categorization function to create the new column
df["Diabetes-level"] = df["Diabetes Value"].apply(categorize_diabetes)
print("Diabetes-level column created.")

# Task 5: Feature selection
# Define target (y) and input (X)
y = df["Diabetes-level"]
X = df.drop(columns=["Diabetes Value", "Diabetes-level"])

# Use SelectKBest with f_classif to select top 5 features
selector = SelectKBest(score_func=f_classif, k=5)
X_new = selector.fit_transform(X, y)

# Get the indices of the selected features
selected_feature_indices = selector.get_support(indices=True)
selected_features = X.columns[selected_feature_indices]

print("Top 5 relevant features for Diabetes-level:")
for feature in selected_features:
    print(feature)

# Optionally, you can further analyze or output the results as needed.

# Save the modified DataFrame back to a CSV file if required
df.to_csv("modified_data.csv", index=False)
