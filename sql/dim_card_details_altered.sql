-- Table: public.dim_card_details

-- DROP TABLE IF EXISTS public.dim_card_details;

CREATE TABLE IF NOT EXISTS public.dim_card_details
(
    card_number text COLLATE pg_catalog."default",
    expiry_date text COLLATE pg_catalog."default",
    card_provider text COLLATE pg_catalog."default",
    date_payment_confirmed text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.dim_card_details
    OWNER to postgres;
	
-- Find the longest value in the card_number column
--SELECT MAX(LENGTH(card_number)) AS max_card_number_length
--FROM dim_card_details;
-- = 22

-- Find the longest value in the expiry_date column
--SELECT MAX(LENGTH(expiry_date)) AS max_expiry_date_length
--FROM dim_card_details;
-- = 10

-- Update data type for card_number to VARCHAR(22)
ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE VARCHAR(22);

-- Update data type for expiry_date to VARCHAR(10)
ALTER TABLE dim_card_details
ALTER COLUMN expiry_date TYPE VARCHAR(10);

-- Set NULL for values explicitly set to 'NULL'
UPDATE dim_card_details
SET date_payment_confirmed = NULL
WHERE date_payment_confirmed !~ '^\d{4}-\d{2}-\d{2}$';

-- Alter the column to the DATE data type
ALTER TABLE dim_card_details
ALTER COLUMN date_payment_confirmed TYPE DATE USING date_payment_confirmed::date;