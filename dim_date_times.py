from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

database_url = 'postgresql://postgres:admin123@localhost:5432/sales_data'

db_connector = DatabaseConnector()
data_cleaner = DataCleaning()
data_extractor = DataExtractor(db_connector)

# Provide the S3 address for the date data
s3_address = 's3://data-handling-public/date_details.json'

# Call the extract_from_s3 method to get the Pandas DataFrame
date_times = data_extractor.extract_json_from_s3(s3_address)

# Display the DataFrame
print(date_times)

# Step 2: Clean the entire DataFrame
#final_cleaned_df = data_cleaner.clean_products_data(date_times)

# Step 3: Clean and convert weights
#cleaned_weights_df = data_cleaner.convert_product_weights(final_cleaned_df)

# Upload to database
db_connector.upload_to_db(date_times, 'dim_date_times', target_database=True)