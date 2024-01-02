-- Database: sales_data

-- DROP DATABASE IF EXISTS sales_data;

CREATE DATABASE sales_data
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

- Remove the £ character from the product_price column
UPDATE dim_products
SET product_price = REPLACE(product_price, '£', '');

-- Add a new column weight_class based on weight ranges
ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR(?); -- Replace ? with the actual max length

-- Update weight_class based on weight ranges
UPDATE dim_products
SET weight_class = 
    CASE
        WHEN weight < 2 THEN 'Light'
        WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
        WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
        WHEN weight >= 140 THEN 'Truck_Required'
    END;

-- Rename the removed column to still_available
ALTER TABLE dim_products
RENAME COLUMN removed TO still_available;

-- Change data types of columns
ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT,
ALTER COLUMN weight TYPE FLOAT,
ALTER COLUMN EAN TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN product_code TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN date_added TYPE DATE,
ALTER COLUMN uuid TYPE UUID,
ALTER COLUMN still_available TYPE BOOL,
ALTER COLUMN weight_class TYPE VARCHAR(?); -- Replace ? with the actual max length

-- Change data types of columns
ALTER TABLE dim_date_times
ALTER COLUMN month TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN year TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN day TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN time_period TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN date_uuid TYPE UUID;

-- Change data types of columns
ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN expiry_date TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN date_payment_confirmed TYPE DATE;

-- Add primary key to dim_users_table
ALTER TABLE dim_users_table
ADD PRIMARY KEY (user_uuid);

-- Add primary key to dim_store_details
ALTER TABLE dim_store_details
ADD PRIMARY KEY (store_code);

-- Add primary key to dim_products
ALTER TABLE dim_products
ADD PRIMARY KEY (product_code);

-- Add primary key to dim_date_times
ALTER TABLE dim_date_times
ADD PRIMARY KEY (date_uuid);

-- Add primary key to dim_card_details
ALTER TABLE dim_card_details
ADD PRIMARY KEY (card_number);

-- Add foreign key constraints in orders_table
ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_dim_users FOREIGN KEY (user_uuid) REFERENCES dim_users_table (user_uuid),
ADD CONSTRAINT fk_orders_dim_store_details FOREIGN KEY (store_code) REFERENCES dim_store_details (store_code),
ADD CONSTRAINT fk_orders_dim_products FOREIGN KEY (product_code) REFERENCES dim_products (product_code),
ADD CONSTRAINT fk_orders_dim_date_times FOREIGN KEY (date_uuid) REFERENCES dim_date_times (date_uuid),
ADD CONSTRAINT fk_orders_dim_card_details FOREIGN KEY (card_number) REFERENCES dim_card_details (card_number);