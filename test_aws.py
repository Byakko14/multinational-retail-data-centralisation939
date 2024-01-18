from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Example usage
aws_access_key = 'AKIAYT5JFYQQZAFAQWRO'
aws_secret_key = 'TmvVKmRdAJH7M6URMI/zdarDiUYT6oXP23oZMb2E'
aws_region = 'eu-west-2'

database_connector = DatabaseConnector()
data_cleaner = DataCleaning()
data_extractor = DataExtractor(database_connector, aws_access_key, aws_secret_key, aws_region)

# Provide the S3 address for the products data
s3_address = 's3://data-handling-public/products.csv'

# Call the extract_from_s3 method to get the Pandas DataFrame
products_data = data_extractor.extract_from_s3(s3_address)

# Display the DataFrame
print(products_data)