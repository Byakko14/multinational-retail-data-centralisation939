-- Table: public.dim_store_details

-- DROP TABLE IF EXISTS public.dim_store_details;

CREATE TABLE IF NOT EXISTS public.dim_store_details
(
    index bigint,
    address text COLLATE pg_catalog."default",
    longitude text COLLATE pg_catalog."default",
    lat text COLLATE pg_catalog."default",
    locality character varying(255) COLLATE pg_catalog."default",
    store_code text COLLATE pg_catalog."default",
    staff_numbers text COLLATE pg_catalog."default",
    opening_date text COLLATE pg_catalog."default",
    store_type text COLLATE pg_catalog."default",
    latitude text COLLATE pg_catalog."default",
    country_code text COLLATE pg_catalog."default",
    continent text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.dim_store_details
    OWNER to postgres;

--UPDATE dim_store_details
--SET longitude = NULL
--WHERE longitude = 'N/A';

--ALTER TABLE dim_store_details
--ALTER COLUMN longitude TYPE FLOAT USING longitude::double precision
--ALTER COLUMN locality TYPE VARCHAR(255)
--ALTER COLUMN store_code TYPE VARCHAR(255)
--ALTER COLUMN staff_numbers TYPE SMALLINT USING staff_numbers::smallint
--ALTER COLUMN opening_date TYPE DATE USING opening_date::date
--DROP COLUMN lat
--ALTER COLUMN latitude TYPE FLOAT USING latitude::double precision
--ALTER COLUMN country_code TYPE VARCHAR(255)
--ALTER COLUMN continent TYPE VARCHAR(255)

UPDATE dim_store_details
SET staff_numbers = NULL
WHERE staff_numbers ~ '[^0-9]'; -- Set NULL for rows with non-numeric values

-- Change the data type of staff_numbers to SMALLINT
ALTER TABLE dim_store_details
ALTER COLUMN staff_numbers TYPE SMALLINT
USING NULLIF(staff_numbers, '')::SMALLINT;
