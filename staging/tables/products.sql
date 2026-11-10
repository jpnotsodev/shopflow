CREATE OR REPLACE TABLE products AS
    SELECT id::INT AS id,
        nullif(name, '') AS name,
        nullif(sku, '') AS sku,
        nullif(category, '') AS category,
        price::DECIMAL(18, 2) AS price
    FROM "sources/products.json";