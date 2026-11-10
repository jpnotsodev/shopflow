CREATE OR REPLACE TABLE customers AS
    SELECT DISTINCT customer_id::INT AS customer_id,
        name,
        email,
        city: concat(upper(trim(city)[1]), lower(trim(city)[2:])),
        date_added::DATE AS date_added
    FROM "sources/customers.csv";