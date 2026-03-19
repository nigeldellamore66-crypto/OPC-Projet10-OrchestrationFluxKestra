CREATE OR REPLACE TABLE web_single AS
SELECT *
FROM web_clean
WHERE post_type='product'