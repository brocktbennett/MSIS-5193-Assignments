import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pycountry  # Import the pycountry library

# MSIS 5193 Assignment 3
# Due Date: Sept 27th (11:59pm)
# Author: Brock Bennett
# Date: Sep 23th, 2023

# Set display options
pd.set_option('display.width', 1000, 'display.max_colwidth', 100, 'display.max_columns', None)

# Load Wine.csv
print("Loading Wine.csv into the dataframe 'Wine_df'...")
file_path1 = "/Users/brocktbennett/GitHub/Project Data/Wine.csv"
wine_df = pd.read_csv(file_path1)
print(f"CSV file loaded successfully with {wine_df.shape[0]} rows and {wine_df.shape[1]} columns.\n")

# Display data types and top 10 rows with the Wine.CSV dataset.
print("Data Types of Each Column:\n", wine_df.dtypes)
print("\nTop 10 Rows of DataFrame:\n", wine_df.head(10))

print("\nTask 1: Using Wine.csv")

# Task 1.1: Bar chart using 'Quality' and 'Alcohol' columns
print("\nTask 1.1: Bar chart using 'Quality' and 'Alcohol' columns.")
quality_alcohol = wine_df.groupby('quality')['alcohol'].mean().sort_values(ascending=False)  # Sort in descending order
sns.barplot(x=quality_alcohol.index, y=quality_alcohol.values, palette='viridis')
plt.title('Average Alcohol Content by Wine Quality')
plt.xlabel('Wine Quality')
plt.ylabel('Average Alcohol Content')
plt.show()

# Task 1.2: Histogram using ‘total sulfur dioxide’
print(f"Description of the column Total Sulfur dioxide")
print(wine_df['total sulfur dioxide'].describe())
print("\nTask 1.2: Histogram using ‘total sulfur dioxide’.")

# Calculate the IQR (Interquartile Range)
# IQR = 75th percentile - 25th percentile
IQR = 64.5 - 23

# Calculate the bin width using the Freedman-Diaconis Rule formula:
# Bin Width = 2 * IQR * (N^(-1/3))
# N is the number of data points, which is 999 in this case.
N = 999
bin_width = 2 * IQR * (N ** (-1/3))

# Print the calculated bin width
print(f"Calculated Bin Width: {bin_width:.2f}")

# Calculate the number of bins based on the bin width
data_range = wine_df['total sulfur dioxide'].max() - wine_df['total sulfur dioxide'].min()
num_bins = int(data_range / bin_width)

# Create the histogram using the calculated number of bins
sns.histplot(wine_df['total sulfur dioxide'], bins=num_bins, color='steelblue', kde=True)
plt.title('Histogram of Total Sulfur Dioxide')
plt.xlabel('Total Sulfur Dioxide')
plt.ylabel('Frequency')
plt.show()

# Task 1.3: Scatter plot using 'residual sugar' and 'quality'
print("\nTask 1.3: Scatter plot using 'residual sugar' and 'quality'.")
sns.scatterplot(data=wine_df, x='residual sugar', y='quality', hue='quality', palette='viridis')
plt.title('Scatter plot of Residual Sugar vs. Quality')
plt.show()

# Task 1.4: Hexbin plot using 'residual sugar' and 'alcohol'
print("\nTask 1.4: Hexbin plot using 'residual sugar' and 'alcohol'.")
plt.hexbin(wine_df['residual sugar'], wine_df['alcohol'], gridsize=30, cmap='viridis')
plt.colorbar(label='Count in Bin')
plt.title('Hexbin plot of Residual Sugar vs. Alcohol Content')
plt.xlabel('Residual Sugar')
plt.ylabel('Alcohol Content')
plt.show()

# Load country_population_historic.csv
print("Task 2: Loading country_population_historic.csv into the dataframe 'country_popdf'...")
file_path2 = "/Users/brocktbennett/GitHub/Project Data/country_population_historic.csv"
country_popdf = pd.read_csv(file_path2)

# Display basic information about the loaded data
print(
    f"Step 2.1: CSV file loaded successfully with {country_popdf.shape[0]} rows and {country_popdf.shape[1]} columns.")
print("Step 2.2: Checking for non-country entries in 'Country Name' column...")
# Get a set of official country names from pycountry
official_country_names = set(country.name for country in pycountry.countries)
# Check for non-country entries and create a filter
non_country_filter = country_popdf['Country Name'].apply(lambda x: x not in official_country_names)
# Apply the filter to exclude non-country entries
df_filtered = country_popdf[~non_country_filter]

# Display data types and top 10 rows of the filtered dataset
print("\nStep 4: Data Types of Each Column in the filtered dataset:\n", df_filtered.dtypes)
print("\nStep 5: Displaying the Top 10 Rows of the filtered DataFrame:\n", df_filtered.head(10))

# Start working on Task 2, using Country_Pop_historic
print("\nStep 6: Task 2 - Analyzing population data (1960-1970) for the top 10 countries.")
# Select the top 10 countries with the highest population in 1960
top10_1960 = df_filtered.nlargest(10, '1960')

# Extract the years from 1960 to 1970 for the top 10 countries
years = [str(year) for year in range(1960, 1971)]
heatmap_data = top10_1960.set_index('Country Name')[years].T

# Display the data for heatmap visualization
print("\nStep 7: Data for Heatmap Visualization:\n", heatmap_data)

# Create a heatmap to visualize population trends
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt="g")
plt.title("Population of Top 10 Countries (1960-1970)")
plt.show()
