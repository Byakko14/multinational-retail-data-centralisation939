from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

database_connector = DatabaseConnector()
data_cleaner = DataCleaning()
data_extractor = DataExtractor(database_connector)

# Provide the S3 address for the products data
s3_address = 's3://data-handling-public/products.csv'

# Call the extract_from_s3 method to get the Pandas DataFrame
products_data = data_extractor.extract_from_s3(s3_address)

# Display the DataFrame
print(products_data)

"""
s3_address = "s3://data-handling-public/products.csv"
bucket, file_from_s3 = s3_address.split('://')[1].split('/', 1)

print("Bucket Name:", bucket)
print("Object Key:", file_from_s3)
"""