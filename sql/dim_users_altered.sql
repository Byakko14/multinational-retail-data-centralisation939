-- Table: public.dim_users

-- DROP TABLE IF EXISTS public.dim_users;

CREATE TABLE IF NOT EXISTS public.dim_users
(
    first_name character varying(20) COLLATE pg_catalog."default",
    last_name character varying(20) COLLATE pg_catalog."default",
    date_of_birth date,
    company text COLLATE pg_catalog."default",
    email_address text COLLATE pg_catalog."default",
    address text COLLATE pg_catalog."default",
    country text COLLATE pg_catalog."default",
    country_code character varying(4) COLLATE pg_catalog."default",
    phone_number double precision,
    join_date timestamp without time zone,
    user_uuid uuid
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.dim_users
    OWNER to postgres;
	
	ALTER TABLE dim_users
ADD COLUMN new_join_date date;

-- Update the new column with the date part of the original 'join_date'
UPDATE dim_users
SET new_join_date = join_date::date;

-- Drop the original 'join_date' column
ALTER TABLE dim_users
DROP COLUMN join_date;

-- Rename the new column to 'join_date'
ALTER TABLE dim_users
RENAME COLUMN new_join_date TO join_date;

-- Create a temporary table to store distinct records
CREATE TEMPORARY TABLE temp_dim_users AS
SELECT DISTINCT ON (user_uuid) *
FROM dim_users;

-- Truncate the original dim_users table
TRUNCATE TABLE dim_users;

-- Insert the distinct records back into dim_users
INSERT INTO dim_users
SELECT * FROM temp_dim_users;

-- Drop the temporary table
DROP TABLE IF EXISTS temp_dim_users;

ALTER TABLE dim_users
ADD CONSTRAINT pk_dim_users_user_uuid PRIMARY KEY (user_uuid);