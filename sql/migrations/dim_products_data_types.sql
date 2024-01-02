-- Change data types of columns in dim_products
ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT,
ALTER COLUMN weight TYPE FLOAT,
ALTER COLUMN EAN TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN product_code TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN date_added TYPE DATE,
ALTER COLUMN uuid TYPE UUID,
ALTER COLUMN still_available TYPE BOOL;

-- Add weight_class column
ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR(?); -- Replace ? with the actual max length
