-- Change data types of columns in dim_date_times
ALTER TABLE dim_date_times
ALTER COLUMN month TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN year TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN day TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN time_period TYPE VARCHAR(?), -- Replace ? with the actual max length
ALTER COLUMN date_uuid TYPE UUID;