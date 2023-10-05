import pandas as pd

# Create example data
data = {
    "Date": [
        "2023-01-01",
        "2023-01-02",
        "2023-01-03",
        "2023-01-04",
        "2023-01-05",
    ],
    "Product": ["A", "B", "A", "C", "B"],
    "Sales": [100, 150, 120, 80, 200],
    "Profit": [30, 40, 25, 10, 50],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("sales_data.csv", index=False)

# Group by Product and calculate total sales and profit
product_group = df.groupby("Product").agg(
    {"Sales": "sum", "Profit": "sum"}
)

# Save the product group to a CSV file
product_group.to_csv("product_group.csv", index=False)

print(
    "Data saved to 'sales_data.csv' and\n"
    "product group data saved to 'product_group.csv'"
)
