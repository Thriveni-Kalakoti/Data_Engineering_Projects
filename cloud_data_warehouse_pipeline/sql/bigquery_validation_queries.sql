-- BigQuery-style validation and analytics queries

-- 1. Row count validation
SELECT
  COUNT(*) AS total_rows
FROM `project_id.dataset_id.ecommerce_orders`;

-- 2. Null key validation
SELECT
  COUNT(*) AS null_key_count
FROM `project_id.dataset_id.ecommerce_orders`
WHERE order_id IS NULL
   OR order_date IS NULL
   OR customer_id IS NULL;

-- 3. Duplicate order_id validation
SELECT
  order_id,
  COUNT(*) AS duplicate_count
FROM `project_id.dataset_id.ecommerce_orders`
GROUP BY order_id
HAVING COUNT(*) > 1;

-- 4. Invalid amount validation
SELECT
  COUNT(*) AS invalid_amount_count
FROM `project_id.dataset_id.ecommerce_orders`
WHERE order_amount <= 0;

-- 5. Revenue by product category
SELECT
  product_category,
  SUM(order_amount) AS total_revenue,
  COUNT(*) AS total_orders
FROM `project_id.dataset_id.ecommerce_orders`
GROUP BY product_category
ORDER BY total_revenue DESC;

-- 6. Monthly revenue trend
SELECT
  order_year,
  order_month,
  SUM(order_amount) AS monthly_revenue,
  COUNT(*) AS monthly_orders
FROM `project_id.dataset_id.ecommerce_orders`
GROUP BY order_year, order_month
ORDER BY order_year, order_month;