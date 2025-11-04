import pandas as pd
from sqlalchemy import create_engine
import psycopg2

df = pd.read_parquet('transformed_ecommerce_data.parquet')  
df.to_csv('transformed_ecommerce_data.csv', index=False)

engine = create_engine("postgresql+psycopg2://admin:adminpassword@localhost:5432/ecommerce_project",
                       connect_args={'client_encoding': 'utf8'}
                       )

df_users = df[["user_id", "name", "email", "location", "is_returning_customer"]].drop_duplicates()
df_users.to_sql("users", engine, if_exists="replace", index=False)

df_products = df[["product", "category"]].drop_duplicates().rename(columns={"product": "product_name"})
df_products.to_sql("products", engine, if_exists="replace", index=False)

df_employees = df[["employee_id", "employee_name"]].drop_duplicates()
df_employees.to_sql("employees", engine, if_exists="replace", index=False)

product_map = pd.read_sql("SELECT product_id, product_name FROM products", engine)
df = df.merge(product_map, left_on="product", right_on="product_name")

df_fact = df[[
    "user_id", "product_id", "employee_id", "price", "quantity", "total_price",
    "payment_method", "device", "delivery_days", "satisfaction_score", "timestamp", "is_high_value"
]]
df_fact.to_sql("transactions", engine, if_exists="replace", index=False)

print("Data loaded into PostgreSQL database successfully.")