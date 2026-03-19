import duckdb
import pandas as pd

con = duckdb.connect("/app/data/bottleneck.duckdb")

df = con.execute("""
    SELECT DISTINCT product_id, post_title, price
    FROM ventes_fusionnees
    WHERE sku NOT LIKE '%bon-cadeau%'
""").df()

mean_price = df["price"].mean()
std_price = df["price"].std(ddof=0)

if std_price == 0:
    df["z_score"] = 0
else:
    df["z_score"] = (df["price"] - mean_price) / std_price

premium = df[df["z_score"] > 2].copy()
ordinaire = df[df["z_score"] <= 2].copy()

premium.to_csv("/app/outputs/vins_premium.csv", index=False)
ordinaire.to_csv("/app/outputs/vins_ordinaires.csv", index=False)