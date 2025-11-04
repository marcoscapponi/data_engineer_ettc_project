from faker import Faker
import random
import csv
import pandas as pd
import numpy as np

fake = Faker()

n = 10000
product_catalog = {
    "Electronics": [
        "Smartphone", "Laptop", "Tablet", "Smartwatch", "Bluetooth Speaker",
        "Wireless Earbuds", "Gaming Console", "Monitor", "External Hard Drive", "Drone"
    ],
    "Clothing": [
        "Jeans", "T-Shirt", "Sneakers", "Jacket", "Dress",
        "Sweater", "Shorts", "Boots", "Scarf", "Cap"
    ],
    "Home": [
        "Blender", "Vacuum Cleaner", "Coffee Maker", "Toaster", "Microwave",
        "Lamp", "Curtains", "Pillow", "Chair", "Desk"
    ],
    "Sports": [
        "Football", "Basketball", "Tennis Racket", "Yoga Mat", "Dumbbells",
        "Running Shoes", "Cycling Helmet", "Swimwear", "Golf Clubs", "Hiking Backpack"
    ],
    "Toys": [
        "Action Figure", "Doll", "Puzzle", "Board Game", "Building Blocks",
        "Remote Control Car", "Stuffed Animal", "Kite", "Yo-Yo", "Water Gun"
    ]
}

name_pool = [fake.name() for _ in range(200)]

name_location_map = {name: fake.city() for name in name_pool}

employee_ids = list(range(1, 51))
employee_names = [fake.name() for _ in range(50)]
employee_map = dict(zip(employee_ids, employee_names))

data = []
for _ in range(n):
    name = random.choice(name_pool)
    location = name_location_map[name]
    category = random.choice(list(product_catalog.keys()))
    product = random.choice(product_catalog[category])
    employee_id = random.choice(employee_ids)
    employee_name = employee_map[employee_id]

    row = {
        "user_id": fake.uuid4(),
        "name": name,
        "email": fake.email(),
        "product": product,
        "category": category,
        "price": round(np.random.uniform(5.0, 100.0), 2),
        "quantity": np.random.randint(1, 5),
        "payment_method": fake.random_element(elements=("Credit Card", "Debit Card", "PayPal", "Bitcoin")),
        "location": location,
        "timestamp": fake.date_time_between(start_date='-5y', end_date='now').isoformat(),
        "device": fake.random_element(elements=("Mobile", "Web", "Shop")),
        "is_returning_customer": fake.boolean(chance_of_getting_true=20),
        "delivery_days": np.random.randint(1, 10),
        "satisfaction_score": np.random.randint(1, 6),
        "employee_id": employee_id,
        "employee_name": employee_name
    }
    data.append(row)

df = pd.DataFrame(data)
df["total_price"] = df["price"] * df["quantity"]

df.to_csv("synthetic_ecommerce_data.csv", index=False)
print("Synthetic data generated and saved to synthetic_ecommerce_data.csv")