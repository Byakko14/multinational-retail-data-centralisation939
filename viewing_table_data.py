from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import pandas as pd

# Assuming db_connector is an instance of DatabaseConnector
db_connector = DatabaseConnector()

# Create a DataExtractor instance
data_extractor = DataExtractor(db_connector)

# List all tables in the database
tables = db_connector.list_db_tables()
print("Tables in the database:", tables)

# Assuming the table containing user data is named 'legacy_users'
user_table_name = 'legacy_users'

# Extract data from the user table
user_data = data_extractor.read_rds_table(user_table_name)

print(user_data)

"""
missing_values = user_data.isnull().sum()
print(missing_values)

index            0
first_name       0
last_name        0
date_of_birth    0
company          0
email_address    0
address          0
country          0
country_code     0
phone_number     0
join_date        0
user_uuid        0
dtype: int64
"""

user_data['date_of_birth'] = pd.to_datetime(user_data['date_of_birth'], errors='coerce')