"""
"Generate a Python script that creates a CSV file with 50 rows of sample customer order data.
 Include columns: order_id, customer_name, email, order_date, amount, status. Include these deliberate data quality issues:
    - 3 rows with null customer_name
    - 2 duplicate order_ids
    - 2 rows with negative amounts
    - 1 row with an invalid email (no @ symbol)
    - 1 row with a future date
    - 1 row with status value not in (pending, completed, cancelled)"

"""


import csv
import random
from datetime import datetime, timedelta

# File name
filename = "sample_data.csv"

# Sample data
first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank"]
last_names = ["Smith", "Doe", "Johnson", "Lee", "Brown", "Davis", "Wilson", "Taylor", "Clark", "Hall"]
statuses = ["pending", "completed", "cancelled"]

def random_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_email(name):
    return name.lower().replace(" ", ".") + "@example.com"

def random_date():
    start_date = datetime(2023, 1, 1)
    return start_date + timedelta(days=random.randint(0, 800))

rows = []

# Generate 50 rows
for i in range(50):
    order_id = 1000 + i
    name = random_name()
    email = random_email(name)
    order_date = random_date().strftime("%Y-%m-%d")
    amount = round(random.uniform(10, 500), 2)
    status = random.choice(statuses)

    rows.append([order_id, name, email, order_date, amount, status])

# ---- Inject Data Quality Issues ----

# 1. 3 rows with null customer_name
for i in [5, 12, 25]:
    rows[i][1] = ""

# 2. 2 duplicate order_ids
rows[10][0] = rows[9][0]
rows[20][0] = rows[19][0]

# 3. 2 rows with negative amounts
rows[15][4] = -50.00
rows[30][4] = -120.75

# 4. 1 row with invalid email (no @)
rows[8][2] = "invalidemail.com"

# 5. 1 row with a future date
future_date = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
rows[35][3] = future_date

# 6. 1 row with invalid status
rows[40][5] = "shipped"

# ---- Write CSV ----
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["order_id", "customer_name", "email", "order_date", "amount", "status"])
    writer.writerows(rows)

print(f"CSV file '{filename}' created with sample data and intentional data quality issues.")