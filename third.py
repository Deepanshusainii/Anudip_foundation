import pandas as pd
import numpy as np

# Set the number of rows and columns
num_rows = 500
num_cols = 7

# Generate random data for each column
np.random.seed(42)  # For reproducibility

# Generate dates
date_range = pd.date_range(start='2023-01-01', periods=num_rows, freq='D')
dates = np.random.choice(date_range, num_rows)

# Generate Product IDs
product_ids = np.random.randint(1000, 2000, size=num_rows)

# Generate Product Names
product_names = [f'Product_{np.random.randint(1, 100)}' for _ in range(num_rows)]

# Generate Sales Quantities
sales_quantities = np.random.randint(1, 100, size=num_rows)

# Generate Unit Prices
unit_prices = np.round(np.random.uniform(5, 100, size=num_rows), 2)

# Calculate Total Sales
total_sales = np.round(sales_quantities * unit_prices, 2)

# Generate Regions
regions = np.random.choice(['North', 'South', 'East', 'West'], num_rows)

# Create the DataFrame
data = {
    'Date': dates,
    'Product ID': product_ids,
    'Product Name': product_names,
    'Sales Quantity': sales_quantities,
    'Unit Price': unit_prices,
    'Total Sales': total_sales,
    'Region': regions
}

df = pd.DataFrame(data)
df.head()
