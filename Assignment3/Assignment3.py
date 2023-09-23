import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
quality_alcohol = wine_df.groupby('quality')['alcohol'].mean().sort_values()
sns.barplot(x=quality_alcohol.index, y=quality_alcohol.values, palette='viridis')
plt.title('Average Alcohol Content by Wine Quality')
plt.xlabel('Wine Quality')
plt.ylabel('Average Alcohol Content')
plt.show()

# Task 1.2: Histogram using ‘total sulfur dioxide’
print("\nTask 1.2: Histogram using ‘total sulfur dioxide’.")
sns.histplot(wine_df['total sulfur dioxide'], bins=30, color='steelblue', kde=True)
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
print("Loading country_population_historic into the dataframe 'country_popdf'....")
file_path2 = "/Users/brocktbennett/GitHub/Project Data/country_population_historic.csv"
country_popdf = pd.read_csv(file_path2)
print(f"CSV file loaded successfully with {country_popdf.shape[0]} rows and {country_popdf.shape[1]} columns.\n")

# List of non-country entries to be dropped
non_countries = [
    "World", "High income", "Arab World", "East Asia & Pacific (excluding high income)",
    "Europe & Central Asia", "Euro area", "European Union", "Latin America & Caribbean",
    "Middle East & North Africa", "Sub-Saharan Africa", "Small states", "OECD members",
    "IDA & IBRD total", "IDA only", "IDA blend", "IBRD only", "Heavily indebted poor countries (HIPC)",
    "Low & middle income", "Middle income", "Upper middle income", "Late-demographic dividend", "East Asia & Pacific",
    "Early-demographic dividend", "Lower middle income", "East Asia & Pacific (IDA & IBRD countries)", "Post-demographic dividend", "IDA total"

]

# Drop the rows corresponding to the non-country entries
df_filtered = country_popdf[~country_popdf['Country Name'].isin(non_countries)]

# Display data types and top 10 rows with the country_pop_historic.CSV dataset.
print("Data Types of Each Column:\n", df_filtered.dtypes)
print("\nTop 10 Rows of DataFrame:\n", df_filtered.head(10))
print(df_filtered.columns)

# Start working on Task 2, using Country_Pop_historic
print("\nTask 2: Using country_population_historic.csv.")
top10_1960 = df_filtered.nlargest(10,'1960')
print(top10_1960)

years = [str(year) for year in range(1960, 1971)]
heatmap_data = top10_1960.set_index('Country Name')[years].T

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt="g")
plt.title("Population of Top 10 Countries (1960-1970)")
plt.show()

