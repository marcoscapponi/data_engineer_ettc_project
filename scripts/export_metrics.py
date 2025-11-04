import pandas as pd

df = pd.read_parquet('transformed_ecommerce_data.parquet')

metrics = {
    "avg_satisfaction": df["satisfaction_score"].mean(),
    "high_value_pct": df["is_high_value"].mean() * 100,
    "avg_ticket": df["total_price"].mean(),
    "total_transactions": len(df)
}

pd.DataFrame([metrics]).to_csv('metrics/metrics.csv', index=False)
print("Metrics exported to metrics/metrics.csv successfully.")