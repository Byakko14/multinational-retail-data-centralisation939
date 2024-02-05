from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import tabula
import pandas as pd

# Create a DataCleaning instance
data_cleaner = DataCleaning()

pdf_link = '/Users/Rit/Workspace/Retail-Data/card_details.pdf'
pdf_data = tabula.read_pdf(pdf_link, pages='all', multiple_tables=True)

#Retrieve data from PDF
db_connector = DatabaseConnector(source_creds_file='db_creds.yaml', target_creds_file='local_db_creds.yaml')
pdf_link = "/Users/Rit/Workspace/Retail-Data/card_details.pdf"
data_extractor = DataExtractor(db_connector)
pdf_data = data_extractor.retrieve_pdf_data(pdf_link)

#print(pdf_data)

#Clean card data
cleaned_card_data = data_cleaner.clean_card_data(pdf_data)

#Upload cleaned data to the database
db_connector.upload_to_db(cleaned_card_data, 'dim_card_details', target_database=True)