import csv
import boto3
import pandas as pd
import tabula
from io import StringIO

class DataExtractor:
    @staticmethod
    def read_rds_table(connector, table_name):
        engine = connector.init_db_engine()
        if table_name not in connector.list_db_tables(engine):
            raise ValueError(f"Table '{table_name}' not found in the database.")
        
        query = f"SELECT * FROM {table_name};"
        return pd.read_sql_query(query, engine)

    @staticmethod
    def retrieve_pdf_data(pdf_url):
        # Use tabula-py to read all pages from the PDF document
        dfs = tabula.read_pdf(pdf_url, pages='all', multiple_tables=True)
        
        # Concatenate all dataframes into one
        extracted_data = pd.concat(dfs, ignore_index=True)
        return extracted_data
    
    @staticmethod
    def list_number_of_stores(endpoint, headers):
        """
        Get the number of stores from the API.

        Parameters:
        - endpoint (str): The number of stores endpoint.
        - headers (dict): Headers for API authentication.

        Returns:
        - int: Number of stores.
        """
        response = requests.get(endpoint, headers=headers)
        return response.json()['count']
    
    @staticmethod
    def retrieve_stores_data(endpoint, headers):
        """
        Retrieve store data from the API and store it in a pandas DataFrame.

        Parameters:
        - endpoint (str): The retrieve a store endpoint.
        - headers (dict): Headers for API authentication.

        Returns:
        - pd.DataFrame: Extracted store data.
        """
        response = requests.get(endpoint, headers=headers)
        stores_data = response.json()
        return pd.DataFrame(stores_data['stores'])

    @staticmethod
    def extract_from_s3(s3_address):
        """
        Extract product information from an S3 bucket.

        Parameters:
        - s3_address (str): S3 address of the CSV file.

        Returns:
        - pd.DataFrame: Extracted product information.
        """
        # Initialize an S3 client
        s3 = boto3.client('s3')

        # Extract data from S3 bucket
        response = s3.get_object(Bucket='data-handling-public', Key='products.csv')
        csv_content = response['Body'].read().decode('utf-8')

        # Read CSV content into a pandas DataFrame
        products_data = pd.read_csv(StringIO(csv_content))
        return products_data