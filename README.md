Personal Expense Tracker
This project simulates a personal expense tracker using synthetic data generated with the Faker library. It stores monthly expenses in an SQL database, analyzes spending patterns through Exploratory Data Analysis (EDA), and visualizes insights using a Streamlit app. The app provides actionable insights into spending behavior, helping users optimize their finances.

Features
Data Simulation: Generate synthetic expense data for a full year using the Faker library.
SQL Integration: Store and query monthly expense data in an SQL database.
Exploratory Data Analysis (EDA): Analyze spending patterns, categorize expenses, and identify trends.
Streamlit Visualization: Interactive web app for visualizing expenses with pie charts, bar charts, and line graphs.
Insights & Recommendations: Provide insights into spending behavior and suggest areas for financial optimization.
Requirements
To run this project locally, you'll need to install the following dependencies:

Python 3.7+
Faker
Pandas
Matplotlib
Seaborn
Streamlit
SQLite (for the database)

INSTALLATION
You can install the necessary packages using pip:

pip install -r requirements.txt

Setup & Usage
Clone the Repository:
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker

Generate Data:

Run the generate_data.py script to create the synthetic expense data:
python generate_data.py

Setup Database:

Run the setup_database.py script to create the SQL database and load the generated data:
python setup_database.py

Run the Streamlit App:

Start the Streamlit app to visualize the data and insights:

streamlit run app.py

SQL Queries:

The project includes 15-20 SQL queries to analyze the data. You can find these in the queries.sql file.

Project Structure

expense-tracker

1.app.py  # Streamlit app

2.generate_data.py    # Script to generate synthetic data

3. setup_database.py   # Script to set up the SQL database
   
4.queries.sql         # SQL queries for analysis

5.requirements.txt    # Python dependencies

6. data/               # Folder to store generated data

7. README.md           # Project documentation

