#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd

# Load the CSV file
df = pd.read_csv('sales_data.csv')

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Print basic statistics of the numerical columns
print("\nBasic statistics of the numerical columns:")
print(df.describe())


# In[18]:


import pandas as pd

# Load the CSV file
df = pd.read_csv('sales_data.csv')

# Calculate the total sales for each region
total_sales_by_region = df.groupby('Region')['Sales'].sum()
print("Total sales for each region:")
print(total_sales_by_region)

# Find the most sold product (based on quantity)
most_sold_product = df.groupby('Product')['Quantity'].sum().idxmax()
print("\nMost sold product (based on quantity):", most_sold_product)

# Compute the average profit margin for each product
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100
average_profit_margin_by_product = df.groupby('Product')['Profit Margin'].mean()
print("\nAverage profit margin for each product:")
print(average_profit_margin_by_product)

