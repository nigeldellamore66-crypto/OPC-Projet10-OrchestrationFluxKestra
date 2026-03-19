CREATE OR REPLACE TABLE ca_global AS
SELECT ROUND(SUM(chiffre_affaires), 2) AS chiffre_affaires_total
FROM ca_par_produit;