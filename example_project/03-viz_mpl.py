import pandas as pd
import matplotlib.pyplot as plt

# Scatter plot of Sales vs. Profit
df = pd.read_csv('sales_data.csv')
plt.figure(figsize=(8, 6))  # Set the figure size
plt.scatter(df['Sales'], df['Profit'])
plt.title('Scatter Plot of Sales vs. Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.savefig('scatter_plot.png')  # Save the figure as a PNG
plt.show()
