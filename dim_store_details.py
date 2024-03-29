from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import requests

database_connector = DatabaseConnector()
data_extractor = DataExtractor(database_connector)
db_connector = DatabaseConnector()
data_cleaner = DataCleaning()

# Example usage
headers = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
number_of_stores_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
retrieve_a_store_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details"

data_extractor.list_number_of_stores(number_of_stores_endpoint, headers)
#print(type(data_extractor.list_number_of_stores(number_of_stores_endpoint, headers)))
number_of_stores = data_extractor.list_number_of_stores(number_of_stores_endpoint, headers)
print(number_of_stores)

#print(type(number_of_stores))

stores_data = data_extractor.retrieve_store_data(retrieve_a_store_endpoint, headers=headers)
print(stores_data)

#Clean store data
cleaned_store_data = data_cleaner.clean_store_data(stores_data)
print(cleaned_store_data)

#Upload cleaned data to the database
#db_connector.upload_to_db(cleaned_store_data, 'dim_store_details', target_database=True)

print(stores_data.isna().sum())