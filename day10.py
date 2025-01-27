#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd

# Load the CSV file
df = pd.read_csv('banking_data.csv')

# Filter out all rows where the Transaction_Amount is greater than 2000
filtered_df = df[df['Transaction_Amount'] <= 2000]
print("Rows where Transaction_Amount is less than or equal to 2000:")
print(filtered_df)

# Find all rows where the Transaction_Type is "Loan Payment" and the Account_Balance is greater than 5000
loan_payment_df = df[(df['Transaction_Type'] == 'Loan Payment') & (df['Account_Balance'] > 5000)]
print("\nRows where Transaction_Type is 'Loan Payment' and Account_Balance is greater than 5000:")
print(loan_payment_df)

# Extract transactions made in the "Uptown" branch
uptown_branch_df = df[df['Branch'] == 'Uptown']
print("\nTransactions made in the 'Uptown' branch:")
print(uptown_branch_df)


# In[24]:


import pandas as pd

# Load the CSV file
df = pd.read_csv('banking_data.csv')

# Add a new column called Transaction_Fee, calculated as 2% of Transaction_Amount
df['Transaction_Fee'] = df['Transaction_Amount'] * 0.02

# Create a new column Balance_Status
df['Balance_Status'] = df['Account_Balance'].apply(lambda x: 'High Balance' if x > 5000 else 'Low Balance')

# Display the updated DataFrame
print(df)

