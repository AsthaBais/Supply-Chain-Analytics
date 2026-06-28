import pandas as pd
from sqlalchemy import create_engine

# ==========================
# CHANGE ONLY THIS PASSWORD
# ==========================
password = "Tiger"

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/supply_chain_analytics"
)

tables = [
    "warehouses",
    "products",
    "customers",
    "orders",
    "inventory",
    "shipments",
    "deliveries"
]

for table in tables:
    print(f"Importing {table}...")

    df = pd.read_csv(f"../Dataset/{table}.csv")

    df.to_sql(
    table,
    con=engine,
    if_exists="replace",   # append ki jagah replace
    index=False
)

    print(f"✅ {table} imported successfully!")

print("\n🎉 All tables imported successfully!")