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