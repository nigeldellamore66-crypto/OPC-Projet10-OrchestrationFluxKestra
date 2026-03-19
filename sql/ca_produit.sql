CREATE OR REPLACE TABLE ca_par_produit AS
SELECT
    product_id,
    post_title,
    price,
    total_sales,
    ROUND(price * total_sales, 2) AS chiffre_affaires
FROM ventes_fusionnees;