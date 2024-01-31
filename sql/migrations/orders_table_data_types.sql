-- Change data types
ALTER TABLE orders_table ALTER COLUMN date_uuid TYPE UUID USING (date_uuid::UUID);
ALTER TABLE orders_table ALTER COLUMN user_uuid TYPE UUID USING (user_uuid::UUID);
ALTER TABLE orders_table ALTER COLUMN card_number TYPE VARCHAR(255); -- Replace 255 with the appropriate length
ALTER TABLE orders_table ALTER COLUMN store_code TYPE VARCHAR(255); -- Replace 255 with the appropriate length
ALTER TABLE orders_table ALTER COLUMN product_code TYPE VARCHAR(255); -- Replace 255 with the appropriate length
ALTER TABLE orders_table ALTER COLUMN product_quantity TYPE SMALLINT;

-- Drop the existing constraints (if any)
ALTER TABLE orders_table DROP CONSTRAINT IF EXISTS orders_table_card_number_check;
ALTER TABLE orders_table DROP CONSTRAINT IF EXISTS orders_table_store_code_check;
ALTER TABLE orders_table DROP CONSTRAINT IF EXISTS orders_table_product_code_check;

-- Add new constraints
ALTER TABLE orders_table ADD CONSTRAINT orders_table_card_number_check CHECK (LENGTH(card_number) <= 255);
ALTER TABLE orders_table ADD CONSTRAINT orders_table_store_code_check CHECK (LENGTH(store_code) <= 255);
ALTER TABLE orders_table ADD CONSTRAINT orders_table_product_code_check CHECK (LENGTH(product_code) <= 255);