import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# MSIS 5193 Assignment 3
# Due Date: Sept 27th (11:59pm)
# Author: Brock Bennett
# Date: Sep 23th, 2023

# Load Wine.csv
print("Loading Wine.csv into the dataframe 'Wine_df'...")
file_path = "/Users/brocktbennett/GitHub/Project Data/Wine.csv"
wine_df = pd.read_csv(file_path)
print(f"CSV file loaded successfully with {wine_df.shape[0]} rows and {wine_df.shape[1]} columns.\n")

# Display data types and top 10 rows
pd.set_option('display.width', 1000, 'display.max_colwidth', 100, 'display.max_columns', None)
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

# Load country_population_historic.csv and Task 2.1
print("\nTask 2: Using country_population_historic.csv.")
file_path_population = "/Users/brocktbennett/GitHub/Project Data/country_population_historic.csv"
population_df = pd.read_csv(file_path_population)
top_10_countries_1960 = population_df.nlargest(10, '1960')






selected_countries = top_10_countries_1960[['Country'] + [str(year) for year in range(1960, 1971)]]
sns.heatmap(selected_countries.set_index('Country'), cmap='YlGnBu', annot=True, fmt="d")
plt.title('Population of Top 10 Countries from 1960 to 1970')
plt.show()
