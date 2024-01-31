-- Table: public.orders_table

-- DROP TABLE IF EXISTS public.orders_table;

CREATE TABLE IF NOT EXISTS public.orders_table
(
    card_number text COLLATE pg_catalog."default",
    expiry_date text COLLATE pg_catalog."default",
    card_provider text COLLATE pg_catalog."default",
    date_payment_confirmed text COLLATE pg_catalog."default",
    unamed_1 double precision,
    product_name text COLLATE pg_catalog."default",
    product_price text COLLATE pg_catalog."default",
    weight text COLLATE pg_catalog."default",
    category text COLLATE pg_catalog."default",
    ean text COLLATE pg_catalog."default",
    date_added text COLLATE pg_catalog."default",
    uuid text COLLATE pg_catalog."default",
    removed text COLLATE pg_catalog."default",
    product_code text COLLATE pg_catalog."default",
    first_name text COLLATE pg_catalog."default",
    last_name text COLLATE pg_catalog."default",
    date_of_birth timestamp without time zone,
    company text COLLATE pg_catalog."default",
    email_address text COLLATE pg_catalog."default",
    address_1 text COLLATE pg_catalog."default",
    country text COLLATE pg_catalog."default",
    country_code_1 text COLLATE pg_catalog."default",
    phone_number double precision,
    join_date timestamp without time zone,
    user_uuid text COLLATE pg_catalog."default",
    index text COLLATE pg_catalog."default",
    address_2 text COLLATE pg_catalog."default",
    longitude text COLLATE pg_catalog."default",
    lat text COLLATE pg_catalog."default",
    locality text COLLATE pg_catalog."default",
    store_code text COLLATE pg_catalog."default",
    staff_numbers text COLLATE pg_catalog."default",
    opening_date text COLLATE pg_catalog."default",
    store_type text COLLATE pg_catalog."default",
    latitude text COLLATE pg_catalog."default",
    country_code_2 text COLLATE pg_catalog."default",
    continent text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.orders_table
    OWNER to postgres;
	
ALTER TABLE orders_table ALTER COLUMN user_uuid TYPE UUID USING (user_uuid::UUID);
ALTER TABLE orders_table ALTER COLUMN card_number TYPE VARCHAR(22);
ALTER TABLE orders_table ALTER COLUMN store_code TYPE VARCHAR(12);
ALTER TABLE orders_table ALTER COLUMN product_code TYPE VARCHAR(11);

-- SELECT MAX(LENGTH(product_code)) AS max_length
-- FROM orders_table;