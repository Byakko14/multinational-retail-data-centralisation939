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

# Concatenate the tables horizontally
merged_data = pd.concat([dim_card_details_data, dim_products_data, dim_users_data, dim_store_details_data], ignore_index=True, axis=1)

max_length = merged_data['0'].str.len().max()

print("Length of the longest cell:", max_length)

"""
df = merged_data.rename(columns={'0': 'card_number', 
                        '1': 'expiry_date',
                        '2': 'card_provider',
                        '3': 'date_payment_confirmed',
                        '4': 'unamed_1',
                        '5': 'product_name',
                        '6': 'product_price',
                        '7': 'weight',
                        '8': 'category',
                        '9': 'EAN', 
                        '10': 'date_added',
                        '11': 'uuid',
                        '12': 'removed',
                        '13': 'product_code',
                        '14': 'first_name',
                        '15': 'last_name',
                        '16': 'date_of_birth',
                        '17': 'company',
                        '18': 'email_address', 
                        '19': 'address_1',
                        '20': 'country',
                        '21': 'country_code_1',
                        '22': 'phone_number',
                        '23': 'join_date',
                        '24': 'user_uuid',
                        '25': 'index',
                        '26': 'address_2',
                        '27': 'longitude', 
                        '28': 'lat',
                        '29': 'locality',
                        '30': 'store_code',
                        '31': 'staff_numbers',
                        '32': 'opening_date',
                        '33': 'store_type',
                        '34': 'latitude',
                        '35': 'country_code_2',
                        '36': 'continent'})

# Drop 'first_name' and 'last_name' columns
#columns_to_remove = ['14', '15']
#df = df.drop(columns=columns_to_remove)

# Display the merged data
print("Merged Data:")
print(df.head())

# Upload to database
db_connector.upload_to_db(df, 'orders_table', target_database=True)
"""