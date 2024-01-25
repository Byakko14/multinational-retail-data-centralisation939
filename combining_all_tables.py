from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import pandas as pd

database_url = 'postgresql://postgres:admin123@localhost:5432/sales_data'

db_connector = DatabaseConnector()
data_cleaner = DataCleaning()
data_extractor = DataExtractor(db_connector)

all_tables = db_connector.list_db_tables(database_url)

print(all_tables)

dim_card_details_data = data_extractor.read_rds_table('dim_card_details')

print(dim_card_details_data)

"""
dim_card_details_data = data_extractor.read_rds_table('dim_card_details')
dim_products_data = data_extractor.read_rds_table('dim_products')
dim_users_data = data_extractor.read_rds_table('dim_users')
dim_store_details_data = data_extractor.read_rds_table('dim_store_details')

# Concatenate the tables vertically
merged_data = pd.concat([dim_card_details_data, dim_products_data, dim_users_data, dim_store_details_data], ignore_index=True)

# Display the merged data
print("Merged Data:")
print(merged_data)

# Upload to database
#db_connector.upload_to_db(cleaned_tables, 'orders_table', target_database=True)
"""