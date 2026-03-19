CREATE OR REPLACE TABLE ventes_fusionnees AS
SELECT
    e.product_id,
    w.sku,
    w.post_title,
    e.stock_quantity,
    e.price,
    w.total_sales 
FROM erp_clean e
INNER JOIN liaison_clean l
  ON e.product_id = l.product_id
INNER JOIN web_single w
  ON l.id_web = w.sku;