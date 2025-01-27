#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd

# Load the CSV file
df = pd.read_csv('banking_data.csv')

# Sort the dataset by Account_Balance in descending order and display the first 10 rows
sorted_df = df.sort_values(by='Account_Balance', ascending=False)
print("First 10 rows of the dataset sorted by Account_Balance in descending order:")
print(sorted_df.head(10))

# Create a ranking column for Transaction_Amount within each Branch
df['Transaction_Rank'] = df.groupby('Branch')['Transaction_Amount'].rank(ascending=False)
print("\nDataFrame with Transaction_Rank column:")
print(df)

