import pandas as pd
import matplotlib.pyplot as plt

# Read product group data from CSV
product_group = pd.read_csv('product_group.csv')

# Bar chart for total sales by product
plt.figure(figsize=(8, 6))  # Set the figure size
product_group['Sales'].plot(kind='bar')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.savefig('sales_by_product.png')  # Save the figure as a PNG
plt.show()
