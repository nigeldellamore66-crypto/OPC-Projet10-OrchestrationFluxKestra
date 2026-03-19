import pandas as pd

files = {
    "/app/data/erp.xlsx": "/app/data/erp.csv",
    "/app/data/web.xlsx": "/app/data/web.csv",
    "/app/data/liaison.xlsx": "/app/data/liaison.csv"
}

for src, dst in files.items():
    df = pd.read_excel(src)
    df.to_csv(dst, index=False)

print("Conversion Excel -> CSV terminée.")