CREATE OR REPLACE TABLE web_clean AS
SELECT DISTINCT
    CAST(sku AS VARCHAR) AS sku,
    CAST(total_sales AS INTEGER) AS total_sales,
    CAST(tax_status AS VARCHAR) AS tax_status,
    CAST(post_title AS VARCHAR) AS post_title,
    CAST(post_excerpt AS VARCHAR) AS post_excerpt,
    CAST(post_name AS VARCHAR) AS post_name,
    CAST(guid AS VARCHAR) AS guid,
    CAST(post_type AS VARCHAR) AS post_type
FROM read_csv_auto('web.csv')
WHERE sku IS NOT NULL