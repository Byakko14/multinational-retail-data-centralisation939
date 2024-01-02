-- Add primary keys to dim tables
ALTER TABLE dim_users_table
ADD PRIMARY KEY (user_uuid);

ALTER TABLE dim_store_details
ADD PRIMARY KEY (store_code);

ALTER TABLE dim_products
ADD PRIMARY KEY (product_code);

ALTER TABLE dim_date_times
ADD PRIMARY KEY (date_uuid);

ALTER TABLE dim_card_details
ADD PRIMARY KEY (card_number);

-- Add foreign key constraints in orders_table
ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_dim_users FOREIGN KEY (user_uuid) REFERENCES dim_users_table (user_uuid),
ADD CONSTRAINT fk_orders_dim_store_details FOREIGN KEY (store_code) REFERENCES dim_store_details (store_code),
ADD CONSTRAINT fk_orders_dim_products FOREIGN KEY (product_code) REFERENCES dim_products (product_code),
ADD CONSTRAINT fk_orders_dim_date_times FOREIGN KEY (date_uuid) REFERENCES dim_date_times (date_uuid),
ADD CONSTRAINT fk_orders_dim_card_details FOREIGN KEY (card_number) REFERENCES dim_card_details (card_number);