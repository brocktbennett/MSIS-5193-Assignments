import mysql.connector
from mysql.connector import Error
import csv
import os

# Constants for database connection
DB_USER = 'readonlyuser'
DB_PASSWORD = 'Msis5193Fall2023'
DB_HOST = '34.70.89.75'
DB_NAME = 'Northwind'

# Constants for file paths
DATA_DIR = '/Users/brocktbennett/GitHub/Project Data/Assignment 4'

# Function to establish and return a MySQL database connection
def establish_connection():
    try:
        cnx = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            database=DB_NAME
        )
        return cnx
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to retrieve and list primary keys and table schemas
def list_primary_keys_and_schemas():
    try:
        # Establish a connection to the database
        cnx = establish_connection()

        if cnx:
            cursor = cnx.cursor()

            # Query to retrieve table names from the database
            query = "SHOW TABLES"

            cursor.execute(query)
            tables = cursor.fetchall()

            for table in tables:
                table_name = table[0]
                print(f"Table: {table_name}")

                # Query to retrieve primary key information for the table
                pk_query = f"SHOW KEYS FROM {table_name} WHERE Key_name = 'PRIMARY'"
                cursor.execute(pk_query)
                primary_keys = cursor.fetchall()
                if primary_keys:
                    print("Primary Key(s):")
                    for pk in primary_keys:
                        print(f"- {pk[4]}")

                # Query to retrieve table schema (column names and data types)
                schema_query = f"DESCRIBE {table_name}"
                cursor.execute(schema_query)
                schema = cursor.fetchall()

                print("Table Schema:")
                for column in schema:
                    print(f"- {column[0]} ({column[1]})")
                print("\n")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if cnx:
            cnx.close()

# Task 1. Export tables Product and Category to CSV files (10 pts)
# Function to export a table to a CSV file
def export_table_to_csv(table_name, filename):
    try:
        # Establish a connection to the database
        cnx = establish_connection()

        if cnx:
            cursor = cnx.cursor()

            # Query to select all rows from the table
            query = f"SELECT * FROM {table_name}"

            cursor.execute(query)
            rows = cursor.fetchall()

            # Export data to a CSV file
            with open(os.path.join(DATA_DIR, filename), 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # Write column headers
                csv_writer.writerows(rows)

            print(f"Table '{table_name}' exported to '{filename}'")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cnx:
            cnx.close()

# Export tables Product and Category to CSV files
export_table_to_csv('Product', 'product.csv')
export_table_to_csv('Category', 'category.csv')

# Function to load data from a CSV file
def load_csv(filename):
    data = []
    try:
        with open(os.path.join(DATA_DIR, filename), 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)  # Read the header row
            for row in csv_reader:
                data.append(row)
        return data
    except FileNotFoundError:
        return []

# Task 2. Use the exported CSV files to find the number of products in each category and save the result into a new CSV file (20 pts)
# Function to count the number of products in each category
def count_products_per_category(product_file, category_file):
    product_data = load_csv(product_file)
    category_data = load_csv(category_file)

    # Create a dictionary to store the counts by category
    category_counts = {}

    for product in product_data:
        category_id = int(product[3])  # Assuming the category ID is in the 4th column
        category_name = None
        for category in category_data:
            if int(category[0]) == category_id:
                category_name = category[1]
                break

        if category_name:
            category_counts.setdefault(category_name, 0)
            category_counts[category_name] += 1

    return category_counts

# Function to save the category counts to a new CSV file
def save_category_counts_to_csv(category_counts, output_filename):
    try:
        with open(os.path.join(DATA_DIR, output_filename), 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Category', 'Count'])
            for category, count in category_counts.items():
                csv_writer.writerow([category, count])
        print(f"Category counts saved to '{output_filename}'")
    except Exception as e:
        print(f"Error: {e}")

# Perform the count and save the result to a new CSV file
product_csv_file = 'product.csv'
category_csv_file = 'category.csv'
category_counts = count_products_per_category(product_csv_file, category_csv_file)
save_category_counts_to_csv(category_counts, 'category_counts.csv')
