import duckdb
import pandas as pd

# Connection à la base DuckDB
con = duckdb.connect("/app/data/bottleneck.duckdb")

# Selection de tout les produits de la table fusionnée 
df = con.execute("""
    SELECT DISTINCT product_id, post_title, price
    FROM ventes_fusionnees
    WHERE sku NOT LIKE '%bon-cadeau%'
""").df()

# Calcul de la moyenne et de l'écart type
mean_price = df["price"].mean()
std_price = df["price"].std(ddof=0)

# Calcul du z_score en fonction de l'écart type
if std_price == 0:
    df["z_score"] = 0
else:
    df["z_score"] = (df["price"] - mean_price) / std_price

# Classification des vins en fonction de leur z_score
premium = df[df["z_score"] > 2].copy()
ordinaire = df[df["z_score"] <= 2].copy()

# Ecriture des fichiers csv
premium.to_csv("/app/outputs/vins_premium.csv", index=False)
ordinaire.to_csv("/app/outputs/vins_ordinaires.csv", index=False)