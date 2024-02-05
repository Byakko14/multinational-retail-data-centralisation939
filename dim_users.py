from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import pandas as pd

# Create a DataCleaning instance
data_cleaner = DataCleaning()

database_url = 'postgresql://postgres:admin123@localhost:5432/sales_data'

# Assuming db_connector is an instance of DatabaseConnector
db_connector = DatabaseConnector(source_creds_file='db_creds.yaml', target_creds_file='local_db_creds.yaml')

# Create a DataExtractor instance
data_extractor = DataExtractor(db_connector)

# Assuming the table containing user data is named 'legacy_users'
user_table_name = 'legacy_users'

# Extract data from the user table
user_data = data_extractor.read_rds_table(user_table_name)

# Clean the user data
cleaned_user_data = data_cleaner.clean_user_data(user_data)

# Display the cleaned user data
print("Cleaned User data:")
print(cleaned_user_data)

# Upload cleaned user data to 'dim_users' table
db_connector.upload_to_db(cleaned_user_data, 'dim_users_test', target_database=True)