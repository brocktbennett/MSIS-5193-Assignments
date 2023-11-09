# MSIS 5193 Assignment 6
# Due Date: Nov 1st (11:59pm – nighttime)
# Author: Brock Bennett
# Date: Oct 20, 2023

# Importing necessary libraries for data handling and analysis
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

# Set display options
pd.set_option('display.width', 1000, 'display.max_colwidth', 100, 'display.max_columns', None)

# Load the dataset for groceries
file_path = "/Users/brocktbennett/GitHub/Project Data/Data Science Programming Data/groceriesARM.csv"
groceries_df = pd.read_csv(file_path, header=None)

# Display the shape of the dataframe to understand the dataset's structure
print("Size of the dataset: ", groceries_df.shape)
print("Number of Transactions: ", groceries_df.shape[0])
print("Number of Items: ", groceries_df.shape[1])

# Fill missing values with 0 to facilitate one-hot encoding later
groceries_df.fillna(0, inplace=True)

# Initialize a set to collect all unique products across transactions
all_products = set()

# Loop over the dataframe to find all unique products
for index, row in groceries_df.iterrows():
    all_products.update(row)

# Display the count and list of unique products
print("Total unique products:", len(all_products))
print("List of products:", all_products)

# Remove the placeholder '0' used for missing items
all_products.discard(0)  # Using discard to avoid KeyError if '0' does not exist

# One Hot Encoding - Transform the dataset into a format suitable for the mining algorithm
encoded_vals = []

for index, row in groceries_df.iterrows():
    rowset = {item: 0 for item in all_products}  # Initialize all products to 0
    rowset.update({item: 1 for item in row if item != 0})  # Set item to 1 if present in the transaction
    encoded_vals.append(rowset)

encoded_vals_df = pd.DataFrame(encoded_vals)

# Using Apriori algorithm to find frequent itemsets with a minimum support threshold
freq_items = apriori(encoded_vals_df, min_support=0.01, use_colnames=True)

# Generate association rules from the frequent itemsets with a minimum confidence threshold
rules = association_rules(freq_items, metric="confidence", min_threshold=0.3)

# Select and display relevant information from the rules
rules = rules[['antecedents', 'consequents', 'support', 'confidence']]
print(rules.sort_values(["confidence", "support"], ascending=[False, False]).reset_index(drop=True).head(35))

# Data Visualization - Plot the support of the frequent itemsets
freq_items['itemsets_str'] = freq_items['itemsets'].apply(lambda x: ', '.join(list(x)))
plt.figure(figsize=(15, 5))
freq_items['support'].plot(kind='bar')
plt.xticks(range(len(freq_items)), freq_items['itemsets_str'], rotation=90)
plt.xlabel('Itemsets')
plt.ylabel('Support')
plt.title('Support of Frequent Itemsets')
plt.show()


