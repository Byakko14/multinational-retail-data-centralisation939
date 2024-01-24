from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

db_connector = DatabaseConnector()
data_cleaner = DataCleaning()
data_extractor = DataExtractor(db_connector)

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