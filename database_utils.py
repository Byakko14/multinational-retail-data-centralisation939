import psycopg2
import yaml
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import tabula

class DatabaseConnector:
    def __init__(self):
        # Initialize the DatabaseConnector with credentials from the YAML file
        self.credentials = self.read_db_creds()

    def read_db_creds(self):
        # Read database credentials from the YAML file
        with open('db_creds.yaml', 'r') as file:
            return yaml.safe_load(file)

    def init_db_engine(self):
        # Initialize and return a SQLAlchemy database engine using credentials
        db_url = f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        return create_engine(db_url)

    def list_db_tables(self, engine):
        # List all tables in the connected database
        inspector = inspect(self._init_db_engine())
        return inspector.get_table_names()

    def upload_to_db(self, engine, table_name, data):
        # Upload data to the specified table in the database
        data.to_sql(table_name, self._init_db_engine(), if_exists='replace', index=False)
