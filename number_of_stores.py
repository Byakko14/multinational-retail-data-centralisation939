from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import requests

database_connector = DatabaseConnector()

data_extractor = DataExtractor(database_connector)

number_of_stores_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
headers = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
store_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}"
retrieve_store_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}"

# Retrieve the number of stores
number_of_stores = data_extractor.list_number_of_stores(number_of_stores_endpoint, headers)

if number_of_stores is not None:
    # Retrieve store data
    stores_data = data_extractor.retrieve_stores_data(retrieve_store_endpoint, headers)

    if stores_data is not None:
        print(f"Number of stores: {number_of_stores}")
        print(stores_data.head())
else:
    print("Failed to retrieve the number of stores.")