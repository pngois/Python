import sqlite3
import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
conn = sqlite3.connect("superstore.db")
df["Order Date"] = pd.to_datetime(df["Order Date"]).dt.strftime("%Y-%m-%d")
df["Ship Date"] = pd.to_datetime(df["Ship Date"]).dt.strftime("%Y-%m-%d")


df.to_sql("orders", conn, if_exists="replace", index=False)
print("Table created with success")