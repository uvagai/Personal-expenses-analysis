import streamlit as st
import mysql.connector
import pandas as pd

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root', 
    'password': 'uvagai@11',  
    'database': 'personel_expenses'  
}

# Function to connect to the database
def get_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

# Function to fetch expenses data from the database
def fetch_expenses_data():
    connection = get_connection()
    if connection:
        query = "SELECT * FROM expenses_all" 
        data = pd.read_sql_query(query, connection) #reads the data into a pandas DataFrame 
        connection.close()
        return data
    else:
        return pd.DataFrame()  

# Function to show graphical representation 
def show_graphs(df):#takes te function dataafra df
    # 1. Bar Chart
    st.subheader("Total Expenses by Category")
    category_data = df.groupby('category')['amount_paid'].sum().reset_index()
    st.bar_chart(category_data.set_index('category'))#plots a bar chart

    # 2. Pie Chart
    st.subheader("Expense Distribution by Category")
    pie_data = category_data.set_index('category')
    st.write(pie_data)

    # 3. Line Chart
    st.subheader("Monthly Expense Trend")
    df['month'] = pd.to_datetime(df['date']).dt.to_period('M')
    monthly_data = df.groupby(df['month'].astype(str))['amount_paid'].sum().reset_index()#using pandas grouping aggregation function
    st.line_chart(monthly_data.set_index('month'))

    # 4. Area Chart
    st.subheader("Cumulative Expense Trend")
    cumulative_data = monthly_data.copy()
    cumulative_data['cumulative_amount'] = cumulative_data['amount_paid'].cumsum()
    st.area_chart(cumulative_data.set_index('month')['cumulative_amount'])

# Streamlit UI setup
st.title("personel expene analyze")
st.write("Welcome to the expense tracker app! Here you can explore your expenses by category and month.")

# Fetch data from the database
expenses_data = fetch_expenses_data()

if not expenses_data.empty:
    st.write("Raw Data from the Database:")
    st.dataframe(expenses_data)

    st.write("Summary Statistics:")
    st.write(expenses_data.describe())#to get summary statistics of a dataset

    show_graphs(expenses_data)
else:
    st.error("Failed to fetch data from the database. Please check your connection or table structure.")
