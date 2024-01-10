from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Assuming db_connector is an instance of DatabaseConnector
db_connector = DatabaseConnector()

# Create a DataExtractor instance
data_extractor = DataExtractor(db_connector)

# List all tables in the database
tables = db_connector.list_db_tables()
print("Tables in the database:", tables)

# Assuming the table containing user data is named 'legacy_users'
user_table_name = 'legacy_users'

# Extract data from the user table
user_data = data_extractor.read_rds_table(user_table_name)

# Display the user data
#print("User data:")
#print(user_data)

"""
Tables in the database: dict_keys(['legacy_store_details', 'legacy_users', 'orders_table'])

Columns in Table: (['index', 'first_name', 'last_name', 'date_of_birth', 'company', 'email_address', 'address', 'country', 'country_code', 'phone_number', 'join_date', 'user_uuid'],
      dtype='object')

User data:
       index first_name  ...   join_date                             user_uuid
0          0   Sigfried  ...  2018-10-10  93caf182-e4e9-4c6e-bebb-60a1a9dcf9b8
1          1        Guy  ...  2001-12-20  8fe96c3a-d62d-4eb5-b313-cf12d9126a49
2          2      Harry  ...  2016-12-16  fc461df4-b919-48b2-909e-55c95a03fe6b
3          3     Darren  ...  2004-02-23  6104719f-ef14-4b09-bf04-fb0c4620acb0
4          4      Garry  ...  2006-09-01  9523a6d3-b2dd-4670-a51a-36aebc89f579
...      ...        ...  ...         ...                                   ...
15315  14913    Stephen  ...  2016-04-15  2bd3a12f-a92d-4cdd-b99c-fc70572db302
15316  14994    Stephen  ...  2020-07-20  d234c04b-c07c-46a5-a902-526f91478ecc
15317  15012    Stephen  ...  2021-03-07  1a0a8b7b-7c17-42d8-a946-8a85d5495651
15318  15269    Stephen  ...  2011-01-03  187fe06e-bd5f-4381-af2f-d7ac37ca7572
15319   1249    Stephen  ...  2015-08-28  0589bbca-1d58-4b1f-9d0a-04ed4c57aaa1

[15320 rows x 12 columns]
"""

# Create a DataCleaning instance
data_cleaner = DataCleaning()

# Clean the user data
cleaned_user_data = data_cleaner.clean_user_data(user_data)

# Display the cleaned user data
print("Cleaned User data:")
print(cleaned_user_data)
print(cleaned_user_data.columns)