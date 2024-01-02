class DataCleaning:
    @staticmethod
    def clean_user_data(data):
        # Method to clean the user data
        pass
        
    @staticmethod
    def clean_card_data(card_data):
        # Method to clean card data
        # Implement cleaning logic here
        cleaned_data = card_data  # Placeholder, replace with actual cleaning logic
        return cleaned_data
    
    @staticmethod
    def _clean_store_data(store_data):
        """
        Clean store data.

        Parameters:
        - store_data (pd.DataFrame): Raw store data.

        Returns:
        - pd.DataFrame: Cleaned store data.
        """
        # Implement cleaning logic here
        # Placeholder, replace with actual cleaning logic
        cleaned_data = store_data
        return cleaned_data
    
    @staticmethod
    def convert_product_weights(products_data):
        """
        Convert and clean the product weights.

        Parameters:
        - products_data (pd.DataFrame): Product data DataFrame.

        Returns:
        - pd.DataFrame: Cleaned product data.
        """
        # Implement weight conversion and cleaning logic here
        # Placeholder, replace with actual conversion and cleaning logic
        cleaned_data = products_data
        return cleaned_data

    @staticmethod
    def clean_products_data(products_data):
        """
        Clean product data.

        Parameters:
        - products_data (pd.DataFrame): Product data DataFrame.

        Returns:
        - pd.DataFrame: Cleaned product data.
        """
        # Implement cleaning logic here
        # Placeholder, replace with actual cleaning logic
        cleaned_data = products_data
        return cleaned_data

    @staticmethod
    def clean_orders_data(orders_data):
        """
        Clean orders table data.

        Parameters:
        - orders_data (pd.DataFrame): Orders data DataFrame.

        Returns:
        - pd.DataFrame: Cleaned orders data.
        """
        # Remove specified columns
        cleaned_orders_data = orders_data.drop(columns=['first_name', 'last_name', '1'], errors='ignore')

        # Cast columns to the correct data types
        data_types = {
            'date_uuid': 'UUID',
            'user_uuid': 'UUID',
            'card_number': 'VARCHAR(16)',  # Replace 16 with the actual max length
            'store_code': 'VARCHAR(?)',   # Replace ? with the actual max length
            'product_code': 'VARCHAR(?)', # Replace ? with the actual max length
            'product_quantity': 'SMALLINT'
        }

        for column, data_type in data_types.items():
            if data_type.startswith('VARCHAR'):
                # Extract the length from the VARCHAR type
                length = int(data_type[data_type.find('(') + 1:data_type.find(')')])
                cleaned_orders_data[column] = cleaned_orders_data[column].astype(data_type.format(length))
            else:
                cleaned_orders_data[column] = cleaned_orders_data[column].astype(data_type)

        return cleaned_orders_data
    
    @staticmethod
    def clean_date_times_data(date_times_data):
        """
        Clean date and time details.

        Parameters:
        - date_times_data (pd.DataFrame): Date and time details DataFrame.

        Returns:
        - pd.DataFrame: Cleaned date and time details.
        """
        # Implement cleaning logic here
        # Placeholder, replace with actual cleaning logic
        cleaned_data = date_times_data
        return cleaned_data
    
    @staticmethod
    def clean_dim_users_data(dim_users_data):
        """
        Clean dim_users_table data.

        Parameters:
        - dim_users_data (pd.DataFrame): dim_users_table DataFrame.

        Returns:
        - pd.DataFrame: Cleaned dim_users_table data.
        """

        # Cast columns to the correct data types
        data_types = {
            'first_name': 'VARCHAR(255)',
            'last_name': 'VARCHAR(255)',
            'date_of_birth': 'DATE',
            'country_code': 'VARCHAR(?)',   # Replace ? with the actual max length
            'user_uuid': 'UUID',
            'join_date': 'DATE'
        }

        for column, data_type in data_types.items():
            if data_type.startswith('VARCHAR'):
                # Extract the length from the VARCHAR type
                length = int(data_type[data_type.find('(') + 1:data_type.find(')')])
                dim_users_data[column] = dim_users_data[column].astype(data_type.format(length))
            else:
                dim_users_data[column] = dim_users_data[column].astype(data_type)

        return dim_users_data
