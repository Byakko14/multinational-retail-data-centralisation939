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

#Retrieve data from API
headers = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
number_of_stores_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
retrieve_a_store_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details"

data_extractor.list_number_of_stores(number_of_stores_endpoint, headers)
number_of_stores = data_extractor.list_number_of_stores(number_of_stores_endpoint, headers)
stores_data = data_extractor.retrieve_store_data(retrieve_a_store_endpoint, headers=headers)

#Clean store data
#cleaned_store_data = data_cleaner.clean_store_data(stores_data)

#Upload cleaned data to the database
#db_connector.upload_to_db(cleaned_store_data, 'dim_store_details', target_database=True)
db_connector.upload_to_db(stores_data, 'dim_store_details', target_database=True)

# Provide the S3 address for the products data
s3_address = 's3://data-handling-public/products.csv'

# Call the extract_from_s3 method to get the Pandas DataFrame
products_data = data_extractor.extract_from_s3(s3_address)

# Display the DataFrame
# print(products_data)

# Step 2: Clean the entire DataFrame
final_cleaned_df = data_cleaner.clean_products_data(products_data)

# Step 3: Clean and convert weights
cleaned_weights_df = data_cleaner.convert_product_weights(final_cleaned_df)

# Upload to database
db_connector.upload_to_db(cleaned_weights_df, 'dim_products', target_database=True)