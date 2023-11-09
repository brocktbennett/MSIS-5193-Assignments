#Importing the Libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

#Read the csv file into a dataframe
groceries_df = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/Data Science Programming Data/groceriesARM.csv",header=None)

#get the shape of dataframe
print("Size of table: ",groceries_df.shape)
print("No of Transactions: ",groceries_df.shape[0])
print("No of items: ",groceries_df.shape[1])

# fill the missing value with 0
groceries_df.fillna(0,inplace=True)

# initialize an empty set to get all unique products
all_products = set()

#Finding all the unique products
for index, row in groceries_df.iterrows():
    # update() method updates the current set, by adding items from row
    all_products.update(row)  # https://www.w3schools.com/python/ref_set_update.asp#:~:text=The%20update()%20method%20updates,present%20in%20the%20updated%20set.
print("Count of products: ",len(all_products))
print("Products: ",all_products)


# Remove '0' from the product list
all_products.remove(0)
print("Count of products: ",len(all_products))
print("Products: ",all_products)

# One Hot Encoding
encoded_vals = list()

# iterate through dataframe to convert each cell into 1 - has product or 0 - no product
for index, row in groceries_df.iterrows():
    # set all cells in a row as 0
    rowset = {item:0 for item in all_products}

    # iterate through the row, if the item is no 0, set the value to be 1
    rowset.update({item:1 for item in row if item != 0})

    # add the rowset to the list
    encoded_vals.append(rowset)

# convert the list into a new dataframe
encoded_vals_df = pd.DataFrame(encoded_vals)
print(encoded_vals_df)

# generate freq item sets using support threshold min_support=0.3
freq_items = apriori(encoded_vals_df, min_support=0.01,use_colnames=True)

# get the rules with confidence threshold set to 0.9
rules = association_rules(freq_items, metric="confidence", min_threshold=0.2)

# get the columns 'antecedents', 'consequents', 'support', 'confidence' from the rules
rules = rules[['antecedents', 'consequents', 'support', 'confidence']]

# sort the rules using "confidence" and "support", and show the top 20 rules
pd.set_option('display.max_columns', None)
print(rules.sort_values(["confidence","support"],ascending=[False, False]).reset_index(drop= True).head(20))
