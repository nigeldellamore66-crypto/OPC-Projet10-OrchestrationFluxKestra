CREATE OR REPLACE TABLE liaison_clean AS
SELECT DISTINCT
    CAST(product_id AS VARCHAR) AS product_id,
    CAST(id_web AS VARCHAR) AS id_web
FROM read_csv_auto('liaison.csv')
WHERE product_id IS NOT NULL;