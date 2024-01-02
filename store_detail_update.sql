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
	
	-- Merge one latitude column into the other
UPDATE store_details_table
SET latitude = COALESCE(latitude1, latitude2)
WHERE latitude IS NULL;

-- Drop the extra latitude column
ALTER TABLE store_details_table
DROP COLUMN IF EXISTS latitude1,
DROP COLUMN IF EXISTS latitude2;

-- Set data types for each column
ALTER TABLE store_details_table
ALTER COLUMN longitude TYPE FLOAT,
ALTER COLUMN locality TYPE VARCHAR(255),
ALTER COLUMN store_code TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN staff_numbers TYPE SMALLINT,
ALTER COLUMN opening_date TYPE DATE,
ALTER COLUMN store_type TYPE VARCHAR(255) NULL,
ALTER COLUMN latitude TYPE FLOAT,
ALTER COLUMN country_code TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN continent TYPE VARCHAR(255);

-- Update location column values where they're null to N/A
UPDATE store_details_table
SET location = 'N/A'
WHERE location IS NULL;