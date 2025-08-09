
---

### Code Sample for Day 9
Below is a single Python file (`Day9_Samples_001.py`) with five sample programs tailored to Module 9: Business Intelligence (Days 41-45), focusing on Day 9's topics of introducing BI, implementing solutions, and data visualization. Note that a sample CSV file (`sales_data.csv`) is assumed; you can create a simple one with columns like `date`, `product`, and `sales` for testing.

```python
# Day9_Samples_001.py
# Program 1: Loading Sales Data
import pandas as pd
data = pd.read_csv("sales_data.csv")
print("First 5 rows of sales data:")
print(data.head())

# Program 2: Calculating Total Sales
total_sales = data["sales"].sum()
print("Total Sales:", total_sales)

# Program 3: Identifying Top Product
top_product = data.loc[data["sales"].idxmax(), "product"]
print("Top Selling Product:", top_product)

# Program 4: Basic Data Visualization with Matplotlib
import matplotlib.pyplot as plt
data["sales"].plot(kind="bar", title="Sales by Entry")
plt.xlabel("Entry")
plt.ylabel("Sales")
plt.show()

# Program 5: Grouping Sales by Product
product_sales = data.groupby("product")["sales"].sum()
product_sales.plot(kind="pie", title="Sales by Product")
plt.ylabel("")  # Remove y-label for pie chart
plt.show()