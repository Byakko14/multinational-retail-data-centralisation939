import pandas as pd
from datetime import datetime

class DataCleaning():
    @staticmethod
    def clean_user_data(data):
        # Drop rows with any NULL values in relevant columns
        relevant_columns = ['first_name', 'last_name', 'date_of_birth', 'company', 'email_address', 'address', 'country', 'country_code', 'phone_number', 'join_date', 'user_uuid']
        cleaned_data = data.dropna(subset=relevant_columns)

        return cleaned_data