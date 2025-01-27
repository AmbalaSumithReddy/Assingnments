#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd

# Load the CSV file
df = pd.read_csv('banking_data.csv')

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Generate basic statistics of the numerical columns
print("\nBasic statistics of the numerical columns:")
print(df.describe())

# Check for missing values in the dataset
print("\nMissing values in the dataset:")
print(df.isnull().sum())


# In[22]:


import pandas as pd

# Load the CSV file
df = pd.read_csv('banking_data.csv')

# Group the data by Account_Type and calculate the total sum of Transaction_Amount
total_transaction_amount_by_account_type = df.groupby('Account_Type')['Transaction_Amount'].sum()
print("Total sum of Transaction_Amount by Account_Type:")
print(total_transaction_amount_by_account_type)

# Calculate the average Account_Balance for each account type
average_account_balance_by_account_type = df.groupby('Account_Type')['Account_Balance'].mean()
print("\nAverage Account_Balance by Account_Type:")
print(average_account_balance_by_account_type)

# Group the data by Branch and calculate the total number of transactions per branch
total_transactions_per_branch = df.groupby('Branch')['Transaction_Amount'].count()
print("\nTotal number of transactions per Branch:")
print(total_transactions_per_branch)

# Calculate the average transaction amount per branch
average_transaction_amount_per_branch = df.groupby('Branch')['Transaction_Amount'].mean()
print("\nAverage Transaction_Amount per Branch:")
print(average_transaction_amount_per_branch)

