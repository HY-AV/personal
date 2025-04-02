# import random
# # import faker
# # import psycopg2
# # from psycopg2 import sql  # Import the sql module

# # Initialize Faker
# # fake = faker.Faker()

# # PostgreSQL connection details
# host = "URL"
# port = 5440  # PostgreSQL default port
# user = "root"
# password = "root"
# database = "pii_info"

# # # Function to generate random PAN card
# # def generate_pan():
# #     return fake.bothify(text='??##??####')

# # # Function to generate random Aadhar number (12 digits, starts with 5)
# # def generate_aadhar():
# #     return '5' + ''.join([str(random.randint(0, 9)) for _ in range(11)])

# # # Function to generate random phone number (Indian format)
# # def generate_phone_number():
# #     return f"+91-{random.randint(7000000000, 9999999999)}"

# # # Function to generate random date of birth
# # def generate_dob():
# #     return fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%Y-%m-%d')

# # # Generate fake personal information
# # def generate_data(num_entries):
# #     return [
# #         (
# #             fake.name(),
# #             generate_pan(),
# #             generate_aadhar(),
# #             fake.email(),
# #             generate_phone_number(),
# #             fake.address().replace("\n", ", "),
# #             generate_dob()
# #         )
# #         for _ in range(num_entries)
# #     ]

# # # Function to create the database if it doesn't exist
# # def create_database_if_not_exists():
# #     try:
# #         conn = psycopg2.connect(
# #             host=host, port=port, user=user, password=password
# #         )
# #         conn.autocommit = True
# #         cursor = conn.cursor()

# #         # Check if the database exists, if not, create it
# #         cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{database}'")
# #         exists = cursor.fetchone()
# #         if not exists:
# #             print(f"Database '{database}' does not exist. Creating the database.")
# #             cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database)))

# #         cursor.close()
# #         conn.close()
# #     except psycopg2.Error as err:
# #         print(f"Error creating database: {err}")

# # # Function to insert data into PostgreSQL
# # def insert_into_postgresql(personal_data):
# #     cursor = None  # Initialize cursor to None to avoid UnboundLocalError
# #     try:
# #         conn = psycopg2.connect(
# #             host=host, port=port, user=user, password=password, dbname=database
# #         )
# #         cursor = conn.cursor()

# #         # Insert Personal Information
# #         insert_query = """
# #             INSERT INTO pii_info (full_name, pan_card, aadhar_number, email, phone_number, address, date_of_birth)
# #             VALUES (%s, %s, %s, %s, %s, %s, %s)
# #         """
# #         cursor.executemany(insert_query, personal_data)
# #         conn.commit()

# #         print(f"{len(personal_data)} fake records inserted successfully!")
# #     except psycopg2.Error as err:
# #         print(f"Error: {err}")
# #     finally:
# #         if cursor:
# #             cursor.close()
# #         conn.close()

# # # Create the database if it doesn't exist
# # create_database_if_not_exists()

# # # Generate and insert 1,000 records
# # personal_data = generate_data(1000)
# # insert_into_postgresql(personal_data)
# import psycopg2
# from faker import Faker
# import random

# # PostgreSQL connection details
# DB_HOST = "URL"
# DB_PORT = "5440"
# DB_USER = "root"
# DB_PASSWORD = "root"
# MAIN_DB = "postgres"  # Connect to this default PostgreSQL database to create others

# # Unique databases and their respective tables
# DATABASES = {
#     "movies_db": ["movies", "directors", "actors", "box_office", "genres"],
#     "finance_db": ["transactions", "accounts", "loans", "customers", "taxes"],
#     "hr_db": ["employees", "departments", "salaries", "attendance", "recruitment"],
#     "ecommerce_db": ["products", "orders", "customers", "reviews", "cart"],
#     "education_db": ["students", "courses", "enrollments", "grades", "teachers"],
#     "pii_db": ["individuals", "addresses", "contacts", "passports", "bank_accounts"],
#     "healthcare_db": ["patients", "doctors", "appointments", "medications", "insurance"],
#     "retail_db": ["stores", "sales", "suppliers", "inventory", "discounts"],
#     "socialmedia_db": ["users", "posts", "comments", "followers", "likes"],
#     "sports_db": ["teams", "players", "matches", "coaches", "stadiums"],
#     "real_estate_db": ["properties", "owners", "rentals", "agents", "mortgages"],
#     "transport_db": ["vehicles", "drivers", "routes", "tickets", "maintenance"],
#     "telecom_db": ["customers", "subscriptions", "calls", "sms", "billing"],
#     "manufacturing_db": ["factories", "workers", "machinery", "production", "shipments"],
#     "government_db": ["citizens", "tax_records", "voter_info", "licenses", "permits"]
# }

# NUM_ROWS_PER_TABLE = 1000
# fake = Faker()

# # Connect to PostgreSQL
# def get_connection(dbname):
#     return psycopg2.connect(
#         dbname=dbname, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
#     )

# # Create databases
# def create_databases():
#     conn = get_connection(MAIN_DB)
#     conn.autocommit = True
#     cur = conn.cursor()

#     for db_name in DATABASES.keys():
#         cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
#         # cur.execute(f"CREATE DATABASE {db_name}")
#         print(f"✅ Created database: {db_name}")

#     cur.close()
#     conn.close()

# # Create tables in each database
# def create_tables():
#     table_schemas = {
#         "movies": "(id SERIAL PRIMARY KEY, title VARCHAR(255), genre VARCHAR(100), release_year INT, director VARCHAR(255), rating FLOAT)",
#         "directors": "(id SERIAL PRIMARY KEY, name VARCHAR(255), nationality VARCHAR(100), birth_date DATE)",
#         "actors": "(id SERIAL PRIMARY KEY, name VARCHAR(255), birth_date DATE, nationality VARCHAR(100))",
#         "box_office": "(id SERIAL PRIMARY KEY, movie_id INT, earnings DECIMAL(10,2))",
#         "genres": "(id SERIAL PRIMARY KEY, genre_name VARCHAR(100))",

#         "transactions": "(id SERIAL PRIMARY KEY, user_id INT, amount DECIMAL(10,2), transaction_date TIMESTAMP, status VARCHAR(50))",
#         "accounts": "(id SERIAL PRIMARY KEY, account_number VARCHAR(20), balance DECIMAL(10,2), customer_id INT)",
#         "loans": "(id SERIAL PRIMARY KEY, loan_id VARCHAR(20), amount DECIMAL(10,2), interest_rate FLOAT, tenure INT)",
#         "customers": "(id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), phone VARCHAR(15))",
#         "taxes": "(id SERIAL PRIMARY KEY, tax_id VARCHAR(20), amount DECIMAL(10,2), year INT)",

#         "employees": "(id SERIAL PRIMARY KEY, full_name VARCHAR(255), department VARCHAR(100), salary DECIMAL(10,2), hire_date DATE)",
#         "departments": "(id SERIAL PRIMARY KEY, department_name VARCHAR(100), manager VARCHAR(255))",
#         "salaries": "(id SERIAL PRIMARY KEY, employee_id INT, amount DECIMAL(10,2))",
#         "attendance": "(id SERIAL PRIMARY KEY, employee_id INT, date DATE, status VARCHAR(10))",
#         "recruitment": "(id SERIAL PRIMARY KEY, job_title VARCHAR(255), applicants INT)",

#         "students": "(id SERIAL PRIMARY KEY, name VARCHAR(255), age INT, grade VARCHAR(10))",
#         "courses": "(id SERIAL PRIMARY KEY, course_name VARCHAR(255), instructor VARCHAR(255))",
#         "enrollments": "(id SERIAL PRIMARY KEY, student_id INT, course_id INT, semester VARCHAR(20))",
#         "grades": "(id SERIAL PRIMARY KEY, student_id INT, course_id INT, grade VARCHAR(5))",
#         "teachers": "(id SERIAL PRIMARY KEY, name VARCHAR(255), subject VARCHAR(100))",
#     }

#     for db_name, tables in DATABASES.items():
#         conn = get_connection(db_name)
#         cur = conn.cursor()

#         for table in tables:
#             schema = table_schemas.get(table, "(id SERIAL PRIMARY KEY, name VARCHAR(255))")
#             cur.execute(f"DROP TABLE IF EXISTS {table}")
#             cur.execute(f"CREATE TABLE {table} {schema}")
#             print(f"✅ Created table {table} in {db_name}")

#         conn.commit()
#         cur.close()
#         conn.close()
# # Insert fake data into tables
# def insert_data():
#     for db_name, tables in DATABASES.items():
#         conn = get_connection(db_name)
#         cur = conn.cursor()

#         for table in tables:
#             for _ in range(NUM_ROWS_PER_TABLE):
#                 if table == "movies":
#                     cur.execute(
#                         f"INSERT INTO {table} (title, genre, release_year, director, rating) VALUES (%s, %s, %s, %s, %s)",
#                         (fake.sentence(), fake.word(), random.randint(1980, 2023), fake.name(), round(random.uniform(1, 10), 1))
#                     )
#                 elif table == "employees":
#                     cur.execute(
#                         f"INSERT INTO {table} (full_name, department, salary, hire_date) VALUES (%s, %s, %s, %s)",
#                         (fake.name(), fake.job(), round(random.uniform(30000, 150000), 2), fake.date_this_decade())
#                     )
#                 elif table == "students":
#                     cur.execute(
#                         f"INSERT INTO {table} (name, age, grade) VALUES (%s, %s, %s)",
#                         (fake.name(), random.randint(10, 25), random.choice(["A", "B", "C", "D"]))
#                     )
#                 elif table == "box_office":
#                     cur.execute(
#                         f"INSERT INTO {table} (movie_id, earnings) VALUES (%s, %s)",
#                         (random.randint(1, 1000), round(random.uniform(100000, 10000000), 2))
#                     )
#                 elif table == "transactions":
#                     cur.execute(
#                         f"INSERT INTO {table} (user_id, amount, transaction_date, status) VALUES (%s, %s, %s, %s)",
#                         (random.randint(1, 1000), round(random.uniform(10, 5000), 2), fake.date_time_this_decade(), random.choice(["Completed", "Pending", "Failed"]))
#                     )
#                 elif table == "accounts":
#                     cur.execute(
#                         f"INSERT INTO {table} (account_number, balance, customer_id) VALUES (%s, %s, %s)",
#                         (fake.bban(), round(random.uniform(1000, 50000), 2), random.randint(1, 1000))
#                     )
#                 else:
#                     # Generic case for tables with a "name" column
#                     cur.execute(f"INSERT INTO {table} (name) VALUES (%s)", (fake.word(),))

#             print(f"✅ Inserted {NUM_ROWS_PER_TABLE} rows into {table} in {db_name}")

#         conn.commit()
#         cur.close()
#         conn.close()

# # Run all steps
# if __name__ == "__main__":
#     # create_databases()
#     # create_tables()
#     # insert_data()
#     print("🎉 Data generation complete!")

import psycopg2
from faker import Faker
import random

# PostgreSQL connection details
DB_HOST = "URL"
DB_PORT = "5440"
DB_USER = "root"
DB_PASSWORD = "root"
MAIN_DB = "postgres"  # Connect to this default PostgreSQL database to create others

# Unique databases and their respective tables
DATABASES = {
    "movies_db": ["movies", "directors", "actors", "box_office", "genres"],
    "finance_db": ["transactions", "accounts", "loans", "customers", "taxes"],
    "hr_db": ["employees", "departments", "salaries", "attendance", "recruitment"],
    "ecommerce_db": ["products", "orders", "customers", "reviews", "cart"],
    "education_db": ["students", "courses", "enrollments", "grades", "teachers"],
    "pii_db": ["individuals", "addresses", "contacts", "passports", "bank_accounts"],
    "healthcare_db": ["patients", "doctors", "appointments", "medications", "insurance"],
    "retail_db": ["stores", "sales", "suppliers", "inventory", "discounts"],
    "socialmedia_db": ["users", "posts", "comments", "followers", "likes"],
    "sports_db": ["teams", "players", "matches", "coaches", "stadiums"],
    "real_estate_db": ["properties", "owners", "rentals", "agents", "mortgages"],
    "transport_db": ["vehicles", "drivers", "routes", "tickets", "maintenance"],
    "telecom_db": ["customers", "subscriptions", "calls", "sms", "billing"],
    "manufacturing_db": ["factories", "workers", "machinery", "production", "shipments"],
    "government_db": ["citizens", "tax_records", "voter_info", "licenses", "permits"]
}

NUM_ROWS_PER_TABLE = 1000
fake = Faker()

# Connect to PostgreSQL
def get_connection(dbname):
    return psycopg2.connect(
        dbname=dbname, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )

# Create databases
def create_databases():
    conn = get_connection(MAIN_DB)
    conn.autocommit = True
    cur = conn.cursor()

    for db_name in DATABASES.keys():
        cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
        cur.execute(f"CREATE DATABASE {db_name}")
        print(f"✅ Created database: {db_name}")

    cur.close()
    conn.close()

# Create tables in each database
def create_tables():
    table_schemas = {
        "movies": "(id SERIAL PRIMARY KEY, title VARCHAR(255), genre VARCHAR(100), release_year INT, director VARCHAR(255), rating FLOAT)",
        "directors": "(id SERIAL PRIMARY KEY, name VARCHAR(255), nationality VARCHAR(100), birth_date DATE)",
        "actors": "(id SERIAL PRIMARY KEY, name VARCHAR(255), birth_date DATE, nationality VARCHAR(100))",
        "box_office": "(id SERIAL PRIMARY KEY, movie_id INT, earnings DECIMAL(10,2))",
        "genres": "(id SERIAL PRIMARY KEY, genre_name VARCHAR(100))",

        "transactions": "(id SERIAL PRIMARY KEY, user_id INT, amount DECIMAL(10,2), transaction_date TIMESTAMP, status VARCHAR(50))",
        "accounts": "(id SERIAL PRIMARY KEY, account_number VARCHAR(50), balance DECIMAL(10,2), customer_id INT)",
        "loans": "(id SERIAL PRIMARY KEY, loan_id VARCHAR(50), amount DECIMAL(10,2), interest_rate FLOAT, tenure INT)",
        "customers": "(id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), phone VARCHAR(20))",
        "taxes": "(id SERIAL PRIMARY KEY, tax_id VARCHAR(50), amount DECIMAL(10,2), year INT)",

        "employees": "(id SERIAL PRIMARY KEY, full_name VARCHAR(255), department VARCHAR(100), salary DECIMAL(10,2), hire_date DATE)",
        "departments": "(id SERIAL PRIMARY KEY, department_name VARCHAR(100), manager VARCHAR(255))",
        "salaries": "(id SERIAL PRIMARY KEY, employee_id INT, amount DECIMAL(10,2))",
        "attendance": "(id SERIAL PRIMARY KEY, employee_id INT, date DATE, status VARCHAR(20))",
        "recruitment": "(id SERIAL PRIMARY KEY, job_title VARCHAR(255), applicants INT)",

        "students": "(id SERIAL PRIMARY KEY, name VARCHAR(255), age INT, grade VARCHAR(10))",
        "courses": "(id SERIAL PRIMARY KEY, course_name VARCHAR(255), instructor VARCHAR(255))",
        "enrollments": "(id SERIAL PRIMARY KEY, student_id INT, course_id INT, semester VARCHAR(20))",
        "grades": "(id SERIAL PRIMARY KEY, student_id INT, course_id INT, grade VARCHAR(5))",
        "teachers": "(id SERIAL PRIMARY KEY, name VARCHAR(255), subject VARCHAR(100))",
    }

    for db_name, tables in DATABASES.items():
        conn = get_connection(db_name)
        cur = conn.cursor()

        for table in tables:
            schema = table_schemas.get(table, "(id SERIAL PRIMARY KEY, name VARCHAR(255))")
            cur.execute(f"DROP TABLE IF EXISTS {table}")
            cur.execute(f"CREATE TABLE {table} {schema}")
            print(f"✅ Created table {table} in {db_name}")

        conn.commit()
        cur.close()
        conn.close()

# Insert fake data into tables
def insert_data():
    for db_name, tables in DATABASES.items():
        conn = get_connection(db_name)
        cur = conn.cursor()

        for table in tables:
            for _ in range(NUM_ROWS_PER_TABLE):
                if table == "movies":
                    cur.execute(
                        f"INSERT INTO {table} (title, genre, release_year, director, rating) VALUES (%s, %s, %s, %s, %s)",
                        (fake.sentence()[:255], fake.word()[:100], random.randint(1980, 2023), fake.name()[:255], round(random.uniform(1, 10), 1))
                    )
                elif table == "directors":
                    cur.execute(
                        f"INSERT INTO {table} (name, nationality, birth_date) VALUES (%s, %s, %s)",
                        (fake.name()[:255], fake.country()[:100], fake.date_of_birth(minimum_age=30, maximum_age=70))
                    )
                elif table == "actors":
                    cur.execute(
                        f"INSERT INTO {table} (name, birth_date, nationality) VALUES (%s, %s, %s)",
                        (fake.name()[:255], fake.date_of_birth(minimum_age=18, maximum_age=70), fake.country()[:100])
                    )
                elif table == "box_office":
                    cur.execute(
                        f"INSERT INTO {table} (movie_id, earnings) VALUES (%s, %s)",
                        (random.randint(1, 1000), round(random.uniform(100000, 10000000), 2))
                    )
                elif table == "genres":
                    cur.execute(
                        f"INSERT INTO {table} (genre_name) VALUES (%s)",
                        (fake.word()[:100],)
                    )
                elif table == "transactions":
                    cur.execute(
                        f"INSERT INTO {table} (user_id, amount, transaction_date, status) VALUES (%s, %s, %s, %s)",
                        (random.randint(1, 1000), round(random.uniform(10, 5000), 2), fake.date_time_this_decade(), random.choice(["Completed", "Pending", "Failed"]))
                    )
                elif table == "accounts":
                    cur.execute(
                        f"INSERT INTO {table} (account_number, balance, customer_id) VALUES (%s, %s, %s)",
                        (fake.bban()[:50], round(random.uniform(1000, 50000), 2), random.randint(1, 1000))
                    )
                elif table == "loans":
                    cur.execute(
                        f"INSERT INTO {table} (loan_id, amount, interest_rate, tenure) VALUES (%s, %s, %s, %s)",
                        (fake.uuid4(), round(random.uniform(1000, 50000), 2), round(random.uniform(1, 10), 2), random.randint(1, 30))
                    )
                elif table == "customers":
                    cur.execute(
                        f"INSERT INTO {table} (name, email, phone) VALUES (%s, %s, %s)",
                        (fake.name()[:255], fake.email()[:255], fake.phone_number()[:15])
                    )
                elif table == "taxes":
                    cur.execute(
                        f"INSERT INTO {table} (tax_id, amount, year) VALUES (%s, %s, %s)",
                        (fake.uuid4(), round(random.uniform(100, 10000), 2), random.randint(2000, 2023))
                    )
                elif table == "employees":
                    cur.execute(
                        f"INSERT INTO {table} (full_name, department, salary, hire_date) VALUES (%s, %s, %s, %s)",
                        (fake.name()[:255], fake.word()[:100], round(random.uniform(30000, 150000), 2), fake.date_this_decade())
                    )
                elif table == "departments":
                    cur.execute(
                        f"INSERT INTO {table} (department_name, manager) VALUES (%s, %s)",
                        (fake.word()[:100], fake.name()[:255])
                    )
                elif table == "salaries":
                    cur.execute(
                        f"INSERT INTO {table} (employee_id, amount) VALUES (%s, %s)",
                        (random.randint(1, 1000), round(random.uniform(30000, 150000), 2))
                    )
                elif table == "attendance":
                    cur.execute(
                        f"INSERT INTO {table} (employee_id, date, status) VALUES (%s, %s, %s)",
                        (random.randint(1, 1000), fake.date_this_decade(), random.choice(["Present", "Absent"]))
                    )
                elif table == "recruitment":
                    cur.execute(
                        f"INSERT INTO {table} (job_title, applicants) VALUES (%s, %s)",
                        (fake.job()[:255], random.randint(1, 100))
                    )
                elif table == "students":
                    cur.execute(
                        f"INSERT INTO {table} (name, age, grade) VALUES (%s, %s, %s)",
                        (fake.name()[:255], random.randint(10, 25), random.choice(["A", "B", "C", "D"]))
                    )
                elif table == "courses":
                    cur.execute(
                        f"INSERT INTO {table} (course_name, instructor) VALUES (%s, %s)",
                        (fake.word()[:255], fake.name()[:255])
                    )
                elif table == "enrollments":
                    cur.execute(
                        f"INSERT INTO {table} (student_id, course_id, semester) VALUES (%s, %s, %s)",
 (random.randint(1, 1000), random.randint(1, 100), random.choice(["Fall", "Spring", "Summer"]))
                    )
                elif table == "grades":
                    cur.execute(
                        f"INSERT INTO {table} (student_id, course_id, grade) VALUES (%s, %s, %s)",
                        (random.randint(1, 1000), random.randint(1, 100), random.choice(["A", "B", "C", "D", "F"]))
                    )
                elif table == "teachers":
                    cur.execute(
                        f"INSERT INTO {table} (name, subject) VALUES (%s, %s)",
                        (fake.name()[:255], fake.word()[:100])
                    )
                else:
                    # Generic case for tables with a "name" column
                    cur.execute(f"INSERT INTO {table} (name) VALUES (%s)", (fake.word()[:255],))

            print(f"✅ Inserted {NUM_ROWS_PER_TABLE} rows into {table} in {db_name}")

        conn.commit()
        cur.close()
        conn.close()

# Run all steps
if __name__ == "__main__":
    create_databases()
    create_tables()
    insert_data()
    print("🎉 Data generation complete!")
