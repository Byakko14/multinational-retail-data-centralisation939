import tabula
import pandas as pd
import requests

class DataExtractor():
    def __init__(self, database_connector):
        self.header = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
        self.base_url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod'

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

    
    def retrieve_store_data(self, retrieve_a_store_endpoint):
        stores_data = []

        # Iterate through each store and retrieve its data
        for store_number in range(1, 452):
            store_url = f"{retrieve_a_store_endpoint}/{store_number}"
            response = requests.get(store_url)

            if response.status_code == 200:
                store_data = response.json()
                stores_data.append(store_data)
            else:
                print(f"Failed to retrieve data for store {store_number}")

        # Convert the list of dictionaries into a DataFrame
        stores_df = pd.DataFrame(stores_data)

        return stores_df
    """

    def retrieve_store_data(self, retrieve_a_store_endpoint):
        stores_data = []

        response = requests.get(f"{retrieve_a_store_endpoint}/{store_number}")
        data = response.json()
        store_detail = data.get('store_details')
        return store_detail
    """