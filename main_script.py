from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Assuming db_connector is an instance of DatabaseConnector
db_connector = DatabaseConnector(source_creds_file='db_creds.yaml', target_creds_file='local_db_creds.yaml')

# Create a DataExtractor instance
data_extractor = DataExtractor(db_connector)

# Assuming the table containing user data is named 'legacy_users'
user_table_name = 'legacy_users'

# Extract data from the user table
user_data = data_extractor.read_rds_table(user_table_name)

# Create a DataCleaning instance
data_cleaner = DataCleaning()

# Clean the user data
cleaned_user_data = data_cleaner.clean_user_data(user_data)

# Display the cleaned user data
print("Cleaned User data:")
print(cleaned_user_data)

# Upload cleaned user data to 'dim_users' table
db_connector.upload_to_db(cleaned_user_data, 'dim_users', target_database=True)

#Retrieve data from PDF
db_connector = DatabaseConnector(source_creds_file='db_creds.yaml', target_creds_file='local_db_creds.yaml')
pdf_link = "/Users/Rit/Workspace/Retail-Data/card_details.pdf"
data_extractor = DataExtractor(db_connector)
pdf_data = data_extractor.retrieve_pdf_data(pdf_link)

#Clean card data
cleaned_card_data = data_cleaner.clean_card_data(pdf_data)

#Upload cleaned data to the database
db_connector.upload_to_db(cleaned_card_data, 'dim_card_details', target_database=True)