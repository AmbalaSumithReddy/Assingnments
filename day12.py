#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('banking_data.csv')

# Plot the total sum of Transaction_Amount per Account_Type using a bar plot
total_transaction_amount_per_account_type = df.groupby('Account_Type')['Transaction_Amount'].sum()
total_transaction_amount_per_account_type.plot(kind='bar', title='Total Transaction Amount per Account Type', xlabel='Account Type', ylabel='Total Transaction Amount', legend=False)
plt.show()

# Create a pie chart to show the percentage of transactions per Branch
transactions_per_branch = df['Branch'].value_counts()
transactions_per_branch.plot(kind='pie', title='Percentage of Transactions per Branch', autopct='%1.1f%%', startangle=90)
plt.ylabel('')  # Hides the y-label
plt.show()

