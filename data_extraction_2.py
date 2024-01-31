import tabula
import pandas as pd
import requests
from sqlalchemy import create_engine
import boto3
from io import StringIO

class DataExtractor():
    def __init__(self, database_connector, database_url): # need to add database_url for orders_data
        self.header = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
        self.base_url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod'
        self.engine = create_engine(database_url) # for extracting and comnbining orders_data
        #self.engine = database_connector.source_engine
        self.database_connector = database_connector

    def read_rds_table(self, table_name):
        """
        Extract the specified database table to a Pandas DataFrame.
        :param table_name: Name of the database table.
        :return: Pandas DataFrame.
        """
        query = f"SELECT * FROM {table_name}"
        return pd.read_sql(query, self.engine)
    
    def retrieve_pdf_data(self, pdf_link):
        # Specify the path to your Java installation
        java_path = '/Library/Java/JavaVirtualMachines/zulu-21.jdk/Contents/Home'

        # Use tabula to extract data from the PDF
        pdf_data = tabula.read_pdf(pdf_link, pages='all', multiple_tables=True)

        # Combine all extracted tables into a single DataFrame
        extracted_data = pd.concat(pdf_data, ignore_index=True)

        return extracted_data
        
    def list_number_of_stores(self, number_of_stores_endpoint, headers):
        response = requests.get(number_of_stores_endpoint, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and return the number of stores
            number_of_stores = data.get('number_stores')
            if number_of_stores is not None:
                return number_of_stores
            else:
                print("Error: 'number_stores' key not found in the response.")
        else:
            print(f"Error: {response.status_code}")
    
    def retrieve_store_data(self, retrieve_a_store_endpoint, headers):
        
        stores_data = []

        # Iterate through each store and retrieve its data
        for store_number in range(0, 451):
            store_url = f"https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}"
            response = requests.get(store_url, headers=headers)

            if response.status_code == 200:
                store_data = response.json()
                stores_data.append(store_data)
            else:
                print(f"Failed to retrieve data for store {store_number}")

        # Convert the list of dictionaries into a DataFrame
        stores_df = pd.DataFrame(stores_data)
       
        return stores_df

    def extract_from_s3(self, s3_address):
        # Create an S3 client
        s3 = boto3.client('s3')

        # Split the S3 address into bucket name and object key
        bucket, file_from_s3 = s3_address.split('://')[1].split('/', 1)

        # Download the file from S3
        response = s3.get_object(Bucket=bucket, Key=file_from_s3)

        # Read CSV data from the response
        csv_data = response['Body'].read().decode('utf-8')

        # Create a Pandas DataFrame from CSV data
        df = pd.read_csv(StringIO(csv_data))

        return df
    
    def extract_json_from_s3(self, s3_address):
        # Create an S3 client
        s3 = boto3.client('s3')

        # Split the S3 address into bucket name and object key
        bucket, file_from_s3 = s3_address.split('://')[1].split('/', 1)

        # Download the file from S3
        response = s3.get_object(Bucket=bucket, Key=file_from_s3)

        # Read JSON data from the response
        json_data = response['Body'].read().decode('utf-8')

        # Create a Pandas DataFrame from JSON data
        df = pd.read_json(StringIO(json_data))

        return df