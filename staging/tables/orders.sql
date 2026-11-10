CREATE OR REPLACE TABLE orders AS
    SELECT CAST(order_id AS VARCHAR) AS order_id,
        customer_id::INTEGER AS customer_id,
        ordered_at::DATETIME AS ordered_at,
        items,
        status
    FROM read_json('data/raw/orders/*/orders.jsonl', hive_partitioning=true)