from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import requests

database_connector = DatabaseConnector()
data_extractor = DataExtractor(database_connector)

# Example usage
number_of_stores_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
headers = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}

data_extractor.list_number_of_stores(number_of_stores_endpoint, headers)
number_of_stores = data_extractor.list_number_of_stores(number_of_stores_endpoint, headers)
print(number_of_stores)


