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