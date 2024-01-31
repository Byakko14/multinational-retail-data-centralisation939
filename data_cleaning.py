import pandas as pd
import re

class DataCleaning():
    @staticmethod
    def clean_user_data(data):
        # Drop rows with any NULL values in relevant columns
        relevant_columns = ['first_name', 'last_name', 'date_of_birth', 'company', 'email_address', 'address', 'country', 'country_code', 'phone_number', 'join_date', 'user_uuid']
        cleaned_data = data.dropna(subset=relevant_columns)

        # Clean date columns ('date_of_birth' and 'join_date')
        date_columns = ['date_of_birth', 'join_date']
        for column in date_columns:
            # Ensure that only valid dates are retained
            cleaned_data[column] = pd.to_datetime(cleaned_data[column], errors='coerce')

        # Drop rows with invalid dates
        cleaned_data = cleaned_data.dropna(subset=date_columns)

        # Convert 'phone_number' to numeric (assuming it's a numeric column)
        cleaned_data['phone_number'] = pd.to_numeric(cleaned_data['phone_number'], errors='coerce')

        # Drop the 'index' column if it exists
        cleaned_data = cleaned_data.drop(columns=['index'], errors='ignore')

        return cleaned_data
    
    def clean_card_data(self, data):
        if data is None:
            # Handle the case where data is None
            return pd.DataFrame()  # or any other appropriate action

        # Drop rows with any NULL values
        cleaned_data = data.dropna()

        return cleaned_data
    
    def clean_store_data(self, data):
        if data is None:
            # Handle the case where data is None
            return pd.DataFrame()  # or any other appropriate action

        # Drop rows with any NULL values
        cleaned_data = data.dropna()

        # Convert date columns to YYYY-MM-DD format
        date_columns = cleaned_data.select_dtypes(include=['datetime']).columns
        cleaned_data[date_columns] = cleaned_data[date_columns].apply(lambda x: x.dt.strftime('%Y-%m-%d'))

        return cleaned_data
    
    def convert_product_weights(self, products_data):
        # Function to clean and convert weights
        def clean_and_convert(weight):
            # Remove excess characters and spaces
            cleaned_weight = re.sub(r'[^\d.]', '', str(weight))

            # Convert to kg
            if 'kg' in str(weight).lower():
                cleaned_weight = float(cleaned_weight)
            elif 'g' in str(weight).lower():
                cleaned_weight = float(cleaned_weight) / 1000  # Convert grams to kilograms
            elif 'ml' in str(weight).lower():
                cleaned_weight = float(cleaned_weight) / 1000  # Convert milliliters to kilograms

            return cleaned_weight

        # Apply the clean_and_convert function to the 'weight' column
        products_data['weight'] = products_data['weight'].apply(clean_and_convert)

        return products_data
    
    def clean_products_data(self, products_data):
        # Drop rows with missing values
        products_data = products_data.dropna()

        # Remove duplicate rows
        products_data = products_data.drop_duplicates()

        return products_data
    
    def clean_orders_data(self, all_tables):
        cleaned_tables = []

        for table_data in all_tables:
            # Assuming each table has a 'first_name', 'last_name', and '1' column
            # If not, you may need to adjust this part based on your actual table structure
            if isinstance(table_data, pd.DataFrame):
                cleaned_table = table_data.drop(columns=['first_name', 'last_name', '1'], errors='ignore')
                cleaned_tables.append(cleaned_table)

        return cleaned_tables