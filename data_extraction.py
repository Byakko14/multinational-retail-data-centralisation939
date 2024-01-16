import tabula
import pandas as pd
import requests

class DataExtractor():
    def __init__(self, database_connector):
        self.engine = database_connector.source_engine
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

    def list_number_of_stores(self, endpoint, headers):
        response = requests.get(endpoint, headers=headers)

        print(f"API Response Code: {response.status_code}")
        print(f"API Response Content: {response.text}")

        if response.status_code == 200:
            try:
                return response.json().get('number_stores')
            except Exception as e:
                print(f"Error parsing response content: {e}")
        else:
            print(f"Failed to retrieve the number of stores. Response content: {response.text}")

        return None
    
    def retrieve_stores_data(self, endpoint, headers):
        # Assuming number_of_stores is obtained from list_number_of_stores
        number_of_stores = self.list_number_of_stores(endpoint, headers)

        if number_of_stores is not None:
            try:
                stores_data = []
                for store_number in range(1, number_of_stores + 1):
                    store_url = f"{endpoint}/{store_number}"  # Correctly construct the URL
                    print(f"Requesting store data from: {store_url}")
                    response = requests.get(store_url, headers=headers)
                    
                    # Check if the response is successful
                    if response.status_code == 200:
                        store_json = response.json()
                        stores_data.append(store_json)
                        print(f"Received store data: {store_json}")
                    else:
                        print(f"Failed to retrieve store data. Response content: {response.content}")

                return stores_data
            except requests.exceptions.RequestException as e:
                print(f"Failed to retrieve store data. Error: {e}")
        else:
            print("Failed to retrieve the number of stores.")
        return None