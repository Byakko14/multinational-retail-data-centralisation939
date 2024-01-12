import tabula
from py4j.java_gateway import java_import, JavaGateway
import pandas as pd
from sqlalchemy import create_engine

class DataExtractor():
    def __init__(self, database_connector):
        self.engine = database_connector.source_engine

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