-- 1. Row count check
SELECT COUNT(*) AS total_rows
FROM sales;

-- 2. Null check for required key columns
SELECT COUNT(*) AS null_key_count
FROM sales
WHERE order_id IS NULL
   OR order_date IS NULL
   OR customer_id IS NULL;

-- 3. Duplicate order_id check
-- SELECT order_id, COUNT(*) AS duplicate_count FROM sales GROUP BY order_id HAVING COUNT(*) > 1;
SELECT COUNT(*) AS duplicate_order_id_count
FROM (
    SELECT order_id
    FROM sales
    GROUP BY order_id
    HAVING COUNT(*) > 1
);

-- 4. Negative sales check
SELECT COUNT(*) AS negative_sales_count
FROM sales
WHERE sales < 0;

-- 5. Invalid quantity check
SELECT COUNT(*) AS invalid_quantity_count
FROM sales
WHERE quantity <= 0;