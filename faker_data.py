#create seperate month data for 12 month

import mysql.connector
from faker import Faker
import random

# Initialize Faker
fake = Faker()


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'uvagai@11',
    'database': 'personel_expenses'  
}


connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Function to create and insert fake data into a table
def create_and_insert_data(month):
    table_name = f"expenses_{month}"
    
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE,
        category VARCHAR(50),
        payment_mode VARCHAR(50),
        description TEXT,
        amount_paid DECIMAL(10, 2),
        cashback DECIMAL(10, 2)
    
    ) AUTO_INCREMENT = 1;
    """
    cursor.execute(create_table_query)
    
    # Insert fake data for 100 records 
    for _ in range(100):
        date = fake.date_this_year()
        category = random.choice(['Food', 'Transportation', 'Bills', 'Groceries', 'Entertainment'])
        payment_mode = random.choice(['Cash', 'Credit Card', 'Debit Card', 'Online'])
        description = fake.text(max_nb_chars=50)
        amount_paid = round(random.uniform(100, 1000), 2)
        cashback = round(random.uniform(10, 100), 2)

        insert_query = f"""
        INSERT INTO {table_name} (date, category, payment_mode, description, amount_paid, cashback)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (date, category, payment_mode, description, amount_paid, cashback))

    connection.commit()

# Loop over the months to create and insert data for 12 months
months = [f"{i:02}" for i in range(1, 13)] 
for month in months:
    create_and_insert_data(month)
cursor.close()
connection.close()
print("month")



#concat all months in one table
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': 'uvagai@11', 
    'database': 'personel_expenses'  
}


connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()


create_combined_table_query = """
CREATE TABLE IF NOT EXISTS expenses_all (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    category VARCHAR(50),
    payment_mode VARCHAR(50),
    description TEXT,
    amount_paid DECIMAL(10, 2),
    cashback DECIMAL(10, 2)
);
"""

cursor.execute(create_combined_table_query)  

# Loop through the months 
months = [f"{i:02}" for i in range(1, 13)] 

for month in months:
    table_name = f"expenses_{month}"

    insert_query = f"""
    INSERT INTO expenses_all (date, category, payment_mode, description, amount_paid, cashback)
    SELECT date, category, payment_mode, description, amount_paid, cashback
    FROM {table_name};
    """
    cursor.execute(insert_query)  

connection.commit()
cursor.close()
connection.close()

print("Data successfully inserted into the 'expenses_all' table.")
