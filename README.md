# Multinational Retail Data Centralization Project

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Database Schema](#database-schema)
- [License](#license)

## Project Overview
This project aims to centralize and manage retail data from multiple sources using a star-based database schema. The data is extracted, cleaned, and stored in a PostgreSQL database using Python scripts.

## Installation
1. Clone this repository.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
Set up your database and configure the credentials in the db_creds.yaml file.
Usage
Run the Python scripts in the following order:

data_extraction.py for extracting data from various sources.
data_cleaning.py for cleaning the extracted data.
database_utils.py for connecting to the database and managing data upload.
main_script.py for orchestrating the data processing flow.
Update the database schema by executing SQL scripts in the sql/migrations folder.

File Structure
lua
Copy code
project_root/
|-- data_extraction.py
|-- data_cleaning.py
|-- database_utils.py
|-- main_script.py
|-- sql/
|   |-- migrations/
|       |-- dim_users_data_types.sql
|       |-- dim_store_details_data_types.sql
|       |-- dim_products_data_types.sql
|       |-- dim_date_times_data_types.sql
|       |-- dim_card_details_data_types.sql
|       |-- primary_keys_foreign_keys.sql
|-- db_creds.yaml
|-- README.md
|-- requirements.txt
Database Schema
The project follows a star-based database schema with the following main tables:

dim_users_table
dim_store_details
dim_products
dim_date_times
dim_card_details
orders_table
For details on data types, primary keys, and foreign keys, refer to the SQL scripts in the sql/migrations folder.

License
This project is licensed under the MIT License.

sql
Copy code

Copy and paste this content into your README.md file. If you have any additional inf