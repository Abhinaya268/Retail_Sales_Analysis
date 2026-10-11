
-- RETAIL SALES ANALYSIS
-- Database: retail_sales_db
-- Table: public.retail_sales

-- 1. Verify total records
SELECT COUNT(*) AS total_records
FROM public.retail_sales;


-- 2. Overall business summary
SELECT
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity,
    ROUND(AVG(discount), 4) AS average_discount
FROM public.retail_sales;


-- 3. Sales and profit by region
SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM public.retail_sales
GROUP BY region
ORDER BY total_sales DESC;


-- 4. Profit by category
SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM public.retail_sales
GROUP BY category
ORDER BY total_profit DESC;


-- 5. Monthly sales and profit
SELECT
    DATE_TRUNC('month', order_date)::date AS sales_month,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM public.retail_sales
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY sales_month;


-- 6. Top 5 profitable sub-categories
SELECT
    sub_category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM public.retail_sales
GROUP BY sub_category
ORDER BY total_profit DESC
LIMIT 5;


-- 7. Profit by discount level
SELECT
    discount,
    COUNT(*) AS record_count,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM public.retail_sales
GROUP BY discount
ORDER BY discount;


-- 8. Top 10 products by sales
SELECT
    product_name,
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM public.retail_sales
GROUP BY product_name, category
ORDER BY total_sales DESC
LIMIT 10;


-- 9. Top 5 customers by profit
SELECT
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM public.retail_sales
GROUP BY customer_name
ORDER BY total_profit DESC
LIMIT 5;


-- 10. Sales and profit by region and category
SELECT
    region,
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM public.retail_sales
GROUP BY region, category
ORDER BY region, total_sales DESC;
