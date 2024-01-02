-- Change data types of columns in dim_users_table
ALTER TABLE dim_users_table
ALTER COLUMN first_name TYPE VARCHAR(255),
ALTER COLUMN last_name TYPE VARCHAR(255),
ALTER COLUMN date_of_birth TYPE DATE,
ALTER COLUMN country_code TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN user_uuid TYPE UUID,
ALTER COLUMN join_date TYPE DATE;