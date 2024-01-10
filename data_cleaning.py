import pandas as pd

class DataCleaning:
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

        # Additional cleaning logic for other columns if needed

        return cleaned_data
    
    def clean_card_data(data):
        # Drop rows with any NULL values
        cleaned_data = data.dropna()