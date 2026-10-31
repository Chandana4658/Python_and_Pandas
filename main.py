
import pandas as pd

# Step 1: Read CSV files
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")

# Step 2: Remove duplicate customers
customers = customers.drop_duplicates(
    subset=["customer_id"]
)

# Step 3: Find invalid customer orders
invalid_orders = orders[
    ~orders["customer_id"].isin(customers["customer_id"])
]

print("Invalid Orders:")
print(invalid_orders)

# Step 4: Join orders with customers
merged_data = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="inner"
)

# Step 5: Join with products
final_data = pd.merge(
    merged_data,
    products,
    on="product_id",
    how="inner"
)

# Step 6: Calculate total amount
final_data["total_amount"] = (
    final_data["quantity"] * final_data["price"]
)

# Step 7: Select required columns
final_orders = final_data[
    [
        "order_id",
        "customer_name",
        "city",
        "product_name",
        "quantity",
        "price",
        "status",
        "total_amount"
    ]
]

# Step 8: Save output
final_orders.to_csv("final_orders.csv", index=False)

print("\nFinal Orders:")
print(final_orders)

print("\nSuccessfully created final_orders.csv")
