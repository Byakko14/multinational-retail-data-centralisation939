from database_utils import DatabaseConnector
from data_extraction_2 import DataExtractor
from data_cleaning import DataCleaning
import pandas as pd

database_url = 'postgresql://postgres:admin123@localhost:5432/sales_data'

db_connector = DatabaseConnector()
data_cleaner = DataCleaning()
data_extractor = DataExtractor(db_connector, database_url)

all_tables = db_connector.list_db_tables(database_url)

print(all_tables)

dim_card_details_data = data_extractor.read_rds_table('dim_card_details')
dim_products_data = data_extractor.read_rds_table('dim_products')
dim_users_data = data_extractor.read_rds_table('dim_users')
dim_store_details_data = data_extractor.read_rds_table('dim_store_details')
dim_date_times_data = data_extractor.read_rds_table('dim_date_times')

# Concatenate the tables horizontally
merged_data = pd.concat([dim_card_details_data, dim_products_data, dim_users_data, dim_store_details_data, dim_date_times_data], ignore_index=True, axis=1)

# Upload to database
db_connector.upload_to_db(merged_data, 'orders_table_test', target_database=True)
