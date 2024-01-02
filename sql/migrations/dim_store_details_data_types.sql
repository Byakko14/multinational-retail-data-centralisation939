-- Change data types of columns in dim_store_details
ALTER TABLE dim_store_details
ALTER COLUMN longitude TYPE FLOAT,
ALTER COLUMN locality TYPE VARCHAR(255),
ALTER COLUMN store_code TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN staff_numbers TYPE SMALLINT,
ALTER COLUMN opening_date TYPE DATE,
ALTER COLUMN store_type TYPE VARCHAR(255) NULL,
ALTER COLUMN latitude TYPE FLOAT,
ALTER COLUMN country_code TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN continent TYPE VARCHAR(255);

-- Update location column where it's null
UPDATE dim_store_details
SET location = 'N/A'
WHERE location IS NULL;