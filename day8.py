#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd

# Load the CSV file
df = pd.read_csv('sales_data.csv')

# Data Filtering
# 1. Extract all rows where sales are greater than 1000
sales_greater_than_1000 = df[df['Sales'] > 1000]
print("Rows where sales are greater than 1000:")
print(sales_greater_than_1000)

# 2. Find all sales records for a specific region (e.g., "East")
sales_in_east_region = df[df['Region'] == 'East']
print("\nSales records for the East region:")
print(sales_in_east_region)

# Data Processing
# 1. Add a new column, Profit_Per_Unit, calculated as Profit / Quantity
df['Profit_Per_Unit'] = df['Profit'] / df['Quantity']
print("\nDataFrame with Profit_Per_Unit column:")
print(df)

# 2. Create another column, High_Sales, which labels rows as Yes if Sales > 1000, else No
df['High_Sales'] = df['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')
print("\nDataFrame with High_Sales column:")
print(df)

