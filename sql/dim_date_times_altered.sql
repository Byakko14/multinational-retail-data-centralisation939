-- Table: public.dim_date_times

-- DROP TABLE IF EXISTS public.dim_date_times;

CREATE TABLE IF NOT EXISTS public.dim_date_times
(
    "timestamp" text COLLATE pg_catalog."default",
    month text COLLATE pg_catalog."default",
    year text COLLATE pg_catalog."default",
    day text COLLATE pg_catalog."default",
    time_period text COLLATE pg_catalog."default",
    date_uuid text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.dim_date_times
    OWNER to postgres;

DELETE FROM dim_date_times
WHERE date_uuid !~ '-';

-- Alter the data type of month to VARCHAR
ALTER TABLE dim_date_times
ALTER COLUMN month TYPE VARCHAR(255);

-- Alter the data type of year to VARCHAR
ALTER TABLE dim_date_times
ALTER COLUMN year TYPE VARCHAR(255);

-- Alter the data type of day to VARCHAR
ALTER TABLE dim_date_times
ALTER COLUMN day TYPE VARCHAR(255);

-- Alter the data type of time_period to VARCHAR
ALTER TABLE dim_date_times
ALTER COLUMN time_period TYPE VARCHAR(255);

-- Alter the data type of date_uuid to UUID
ALTER TABLE dim_date_times
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::uuid;

-- Adding primary key
ALTER TABLE dim_date_times
ADD CONSTRAINT pk_dim_date_times_date_uuid PRIMARY KEY (date_uuid);