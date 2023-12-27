from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import boto3
import pandas as pd
from io import StringIO

# Create instances
connector = DatabaseConnector()
extractor = DataExtractor()
cleaner = DataCleaning()

# PDF document link
pdf_link = 'your_pdf_link_here'

# Retrieve card data from PDF
card_data = extractor.retrieve_pdf_data(pdf_link)

# Clean card data
cleaned_card_data = cleaner.clean_card_data(card_data)

# Upload cleaned card data to the database
engine = connector.init_db_engine()
connector.upload_to_db(engine, 'dim_card_details', cleaned_card_data)

# API details
number_of_stores_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
api_headers = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
retrieve_stores_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'

# Get the number of stores
num_stores = extractor.list_number_of_stores(number_of_stores_endpoint, api_headers)
print(f"Number of stores: {num_stores}")

# Retrieve store data from the API
stores_data = extractor.retrieve_stores_data(retrieve_stores_endpoint, api_headers)

# Clean store data
cleaned_stores_data = cleaner._clean_store_data(stores_data)

# Upload cleaned store data to the database
engine = connector.init_db_engine()
connector.upload_to_db(engine, 'dim_store_details', cleaned_stores_data)

# S3 address for products data
s3_products_address = 's3://data-handling-public/products.csv'

# Extract product data from S3
products_data = extractor.extract_from_s3(s3_products_address)

# Convert and clean product weights
converted_products_data = cleaner.convert_product_weights(products_data)

# Clean product data
cleaned_products_data = cleaner.clean_products_data(converted_products_data)

# Upload cleaned product data to the database
engine = connector.init_db_engine()
connector.upload_to_db(engine, 'dim_products', cleaned_products_data)

# List all tables in the connected database
engine = connector.init_db_engine()
tables = connector.list_db_tables(engine)
print("Tables in the database:", tables)

# Get the name of the table containing orders data
orders_table_name = 'your_orders_table_name'  # Replace with the actual table name

# Extract orders data from the RDS database
orders_data = extractor.read_rds_table(connector, orders_table_name)

# Clean orders data
cleaned_orders_data = cleaner.clean_orders_data(orders_data)

# Upload cleaned orders data to the database
engine = connector.init_db_engine()
connector.upload_to_db(engine, 'orders_table', cleaned_orders_data)

@staticmethod
def extract_from_s3_json(s3_link):
    """
    Extract date and time details from a JSON file on S3.

    Parameters:
    - s3_link (str): S3 link to the JSON file.

    Returns:
    - pd.DataFrame: Extracted date and time details.
    """
    # Initialize an S3 client
    s3 = boto3.client('s3')

    # Extract data from S3 bucket
    response = s3.get_object(Bucket='data-handling-public', Key='date_details.json')
    json_content = response['Body'].read().decode('utf-8')

    # Read JSON content into a pandas DataFrame
    date_times_data = pd.read_json(StringIO(json_content))
    return date_times_data

# S3 link for date and time details
s3_date_times_link = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'

# Extract date and time details from the JSON file on S3
date_times_data = extractor.extract_from_s3_json(s3_date_times_link)

# Clean date and time details
cleaned_date_times_data = cleaner.clean_date_times_data(date_times_data)

# Upload cleaned date and time details to the database
engine = connector.init_db_engine()
connector.upload_to_db(engine, 'dim_date_times', cleaned_date_times_data)

orders_table = DataCleaning.clean_orders_data(orders_table)

dim_users_table = DataCleaning.clean_dim_users_data(dim_users_table)