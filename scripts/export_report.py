import duckdb
import pandas as pd

# Connection à la base duckDB
con = duckdb.connect("/app/data/bottleneck.duckdb")

# Récupération des chiffres d'affaires sur les 2 tables produites
df_ca = con.execute("SELECT * FROM ca_par_produit ORDER BY chiffre_affaires DESC").df()
df_total = con.execute("SELECT * FROM ca_global").df()

# Ecriture des chiffres d'affaires sur 1 fichier excel, dans 2 sheet séparées
with pd.ExcelWriter("/app/outputs/rapport_chiffre_affaires.xlsx", engine="openpyxl") as writer:
    df_ca.to_excel(writer, sheet_name="CA_par_produit", index=False)
    df_total.to_excel(writer, sheet_name="CA_global", index=False)

print("Export rapport_chiffre_affaires.xlsx OK.")