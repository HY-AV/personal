import random
import faker
import mysql.connector

# Initialize Faker
fake = faker.Faker()

# # MySQL connection details
# host = "URL"
# port = 3307  # MySQL port
# user = "root"
# password = "root"
# database = "eCom"

# # Function to generate random PAN card
# def generate_pan():
#     return fake.bothify(text='??##??####')

# # Function to generate random Aadhar number starting with 5
# def generate_aadhar():
#     return '5' + ''.join([str(random.randint(0, 9)) for _ in range(11)])

# # Function to generate random phone number
# def generate_phone_number():
#     return f"+91-{random.randint(7000000000, 9999999999)}"

# # Function to generate random date of birth
# def generate_dob():
#     return fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%Y-%m-%d')

# # Generate 1,000 fake personal information entries
# def generate_data(num_entries):
#     personal_data = []
#     for _ in range(num_entries):
#         # Personal Information
#         full_name = fake.name()
#         pan_card = generate_pan()
#         aadhar_number = generate_aadhar()
#         email = fake.email()
#         phone_number = generate_phone_number()
#         address = fake.address().replace("\n", ", ")
#         dob = generate_dob()

#         personal_data.append((full_name, pan_card, aadhar_number, email, phone_number, address, dob))

#     return personal_data

# # Function to insert data into MySQL
# def insert_into_mysql(personal_data):
#     # Connect to MySQL database
#     conn = mysql.connector.connect(
#         host=host,
#         port=port,
#         user=user,
#         password=password,
#         database=database
#     )
#     cursor = conn.cursor()

#     # Insert Personal Information
#     insert_query = """
#         INSERT INTO pii_info (full_name, pan_card, aadhar_number, email, phone_number, address, date_of_birth)
#         VALUES (%s, %s, %s, %s, %s, %s, %s)
#     """
#     cursor.executemany(insert_query, personal_data)
#     conn.commit()
#     cursor.close()
#     conn.close()

# # Generate 1,000 records
# personal_data = generate_data(1000)

# # Insert the generated data into the MySQL database
# insert_into_mysql(personal_data)

# print("1,000 fake records (personal info) inserted into MySQL database.")

import os
import pandas as pd
import mysql.connector
import re  # Regular expression module

# MySQL connection details
host = "URL"
port = 3307  # MySQL port
user = "root"
password = "root"
database = "ecom_web_db"

# Path to the folder containing CSV files
csv_folder = "dummy_csv"

# Function to create database if not exists
def create_database_if_not_exists():
    try:
        # Connect to MySQL without specifying a database (root level connection)
        conn = mysql.connector.connect(
            host=host, port=port, user=user, password=password
        )
        cursor = conn.cursor()

        # Check if the database exists and create it if it does not
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database};")
        conn.commit()
        print(f"Database '{database}' is ready!")

    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
    finally:
        cursor.close()
        conn.close()

# Function to read the first 200 rows from all CSV files in the folder
def read_csv_files(csv_folder):
    csv_files = [file for file in os.listdir(csv_folder) if file.endswith(".csv")]
    data_frames = []
    
    for csv_file in csv_files:
        file_path = os.path.join(csv_folder, csv_file)
        try:
            # Try reading the first 200 rows of the CSV file with 'utf-8' encoding first
            df = pd.read_csv(file_path, encoding='utf-8', nrows=200)
        except UnicodeDecodeError:
            # If a UnicodeDecodeError occurs, try reading with 'latin1' encoding
            df = pd.read_csv(file_path, encoding='latin1', nrows=200)
        
        # Store both the cleaned file name (without .csv) and DataFrame
        table_name = os.path.splitext(csv_file)[0]  # Remove .csv extension
        data_frames.append((table_name, df))
    
    return data_frames

# Function to clean the table/column names by replacing spaces with underscores and removing numeric suffixes
def clean_name(name):
    # Remove numeric suffixes in parentheses like (2)
    cleaned_name = re.sub(r'\(\d+\)', '', name)
    # Replace spaces with underscores
    cleaned_name = cleaned_name.replace(" ", "_")
    # Remove trailing underscores if they exist
    cleaned_name = cleaned_name.rstrip("_")
    return cleaned_name

# Function to create table and insert data into MySQL
def create_table_and_insert_data(df, table_name):
    try:
        # Clean the table name (remove numeric suffixes and spaces)
        cleaned_table_name = clean_name(table_name)
        
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host=host, port=port, user=user, password=password, database=database
        )
        cursor = conn.cursor()

        # Clean the column names
        cleaned_columns = [clean_name(col) for col in df.columns]

        # Create a table query based on the cleaned column names
        create_table_query = f"CREATE TABLE IF NOT EXISTS `{cleaned_table_name}` (" + ", ".join(
            [f"`{col}` VARCHAR(255)" for col in cleaned_columns]
        ) + ");"
        cursor.execute(create_table_query)
        
        # Insert data into the table
        for _, row in df.iterrows():
            insert_query = f"INSERT INTO `{cleaned_table_name}` ({', '.join(cleaned_columns)}) VALUES ({', '.join(['%s' for _ in cleaned_columns])})"
            cursor.execute(insert_query, tuple(row))

        # Commit changes
        conn.commit()
        print(f"Table '{cleaned_table_name}' created and data inserted successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()


# Create database if it does not exist
create_database_if_not_exists()

# Read data from all CSV files in the folder
data_frames = read_csv_files(csv_folder)

# Iterate through each DataFrame and insert data into corresponding table
for table_name, df in data_frames:
    create_table_and_insert_data(df, table_name)
