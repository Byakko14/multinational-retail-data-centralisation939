-- Table: public.dim_products

-- DROP TABLE IF EXISTS public.dim_products;

CREATE TABLE IF NOT EXISTS public.dim_products
(
    "Unnamed: 0" bigint,
    product_name text COLLATE pg_catalog."default",
    product_price text COLLATE pg_catalog."default",
    weight text COLLATE pg_catalog."default",
    category text COLLATE pg_catalog."default",
    "EAN" text COLLATE pg_catalog."default",
    date_added text COLLATE pg_catalog."default",
    uuid text COLLATE pg_catalog."default",
    removed text COLLATE pg_catalog."default",
    product_code text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.dim_products
    OWNER to postgres;

UPDATE dim_products
SET product_price = REPLACE(product_price, '£', '');
UPDATE dim_products
SET product_price = NULL WHERE product_price ~ '[^0-9.]';
UPDATE dim_products
SET date_added = 
    CASE 
        WHEN date_added ~ '^\d{4}-\d{2}-\d{2}$' THEN date_added -- Keep valid values
        ELSE NULL -- Set NULL for rows with non-matching values
    END;

ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT USING product_price::double precision

ALTER TABLE dim_products
ALTER COLUMN weight TYPE FLOAT USING weight::double precision

ALTER TABLE dim_products
ALTER COLUMN "EAN" TYPE VARCHAR(255)

ALTER TABLE dim_products
ALTER COLUMN product_code TYPE VARCHAR(255)

ALTER TABLE dim_products
ALTER COLUMN date_added TYPE date USING date_added::date

DELETE FROM dim_products
WHERE uuid IN ('7QB0Z9EW1G', 'CP8XYQVGGU', 'VIBLHHVPMN');	

ALTER TABLE dim_products
ALTER COLUMN uuid TYPE UUID USING uuid::uuid

ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR(255); -- Adjust the length as needed
-- Update weight_class based on weight range
UPDATE dim_products
SET weight_class =
    CASE 
        WHEN weight < 2 THEN 'Light'
        WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
        WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
        WHEN weight >= 140 THEN 'Truck_Required'
        ELSE NULL -- Handle any other cases as needed
    END;
	
ALTER TABLE dim_products
RENAME COLUMN removed TO still_available;

UPDATE dim_products
SET still_available = (CASE 
                        WHEN still_available = 'Still_avaliable' THEN true 
                        WHEN still_available = 'Removed' THEN false
                      END);

ALTER TABLE dim_products
ALTER COLUMN still_available TYPE BOOLEAN USING still_available::boolean;