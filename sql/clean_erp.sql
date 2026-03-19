CREATE OR REPLACE TABLE erp_clean AS
SELECT DISTINCT
    CAST(product_id AS VARCHAR) AS product_id,
    CAST(onsale_web AS INTEGER) AS onsale_web,
    CAST(price AS DOUBLE) AS price,
    CAST(stock_quantity AS INTEGER) AS stock_quantity,
    CAST(stock_status AS VARCHAR) AS stock_status
FROM read_csv_auto('erp.csv')
WHERE product_id IS NOT NULL
  AND price IS NOT NULL;