import pandas as pd
import yaml
from sqlalchemy import create_engine, inspect

class DatabaseConnector():
    def __init__(self, source_creds_file='db_creds.yaml', target_creds_file='local_db_creds.yaml'):
        self.source_credentials = self.read_db_creds(source_creds_file)
        self.source_engine = self.init_db_engine(self.source_credentials)

        if target_creds_file:
            self.target_credentials = self.read_db_creds(target_creds_file)
            self.target_engine = self.init_db_engine(self.target_credentials)
        else:
            self.target_credentials = None
            self.target_engine = None

    def read_db_creds(self, creds_file):
        """
        Read database credentials from the YAML file and return a dictionary.
        :param creds_file: Path to the YAML file containing credentials.
        :return: Dictionary of database credentials.
        """
        with open(creds_file, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials

    def init_db_engine(self, credentials):
        """
        Initialize and return an SQLAlchemy database engine with the loaded credentials.
        :return: SQLAlchemy database engine.
        """
        database_url = f'postgresql://{credentials["RDS_USER"]}:{credentials["RDS_PASSWORD"]}@{credentials["RDS_HOST"]}:{credentials["RDS_PORT"]}/{credentials["RDS_DATABASE"]}'
        return create_engine(database_url)

    def list_db_tables(self, target_database=False):
        """
        List all tables in the database.
        :return: List of table names.
        """
        engine = self.target_engine if target_database else self.source_engine
        return self.get_table_names(engine)
    
    def get_table_names(self, engine):
        inspector = inspect(engine)
        return inspector.get_table_names()

    def upload_to_db(self, data, table_name, target_database=False):
        data = data.copy()
        """
        Upload data to the specified table in the database.
        If the table does not exist, create it.
        :param data: Pandas DataFrame containing data to upload.
        :param table_name: Name of the table to upload to.
        :param target_database: True if uploading to the target database, False if uploading to the source database.
        """
        engine = self.target_engine if target_database else self.source_engine

        # Reset index before uploading to avoid datatype mismatch
        data.reset_index(drop=True, inplace=True)

        if table_name not in self.list_db_tables(target_database=target_database):
            # Table does not exist, create it based on the structure of the DataFrame
            data.head(0).to_sql(name=table_name, con=engine, if_exists='replace', index=False)

        # Drop 'index' column if it exists before uploading
        data.drop(columns=['index'], errors='ignore', inplace=True)

        # Upload data to the table
        data.to_sql(name=table_name, con=engine, if_exists='append', index=False)