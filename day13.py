#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Day_13_Pharma_data.csv')

# Perform data cleaning
# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# Check for duplicates
print("\nDuplicates:")
print(df.duplicated().sum())

# Drop duplicates
df = df.drop_duplicates()

# Visualizations
# 1. Bar plot showing total sales per region
total_sales_per_region = df.groupby('Region')['Sales'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=total_sales_per_region)
plt.title('Total Sales per Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

# 2. Scatter plot to visualize the relationship between Marketing_Spend and Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Marketing_Spend', y='Sales', data=df, hue='Region')
plt.title('Relationship between Marketing Spend and Sales')
plt.xlabel('Marketing Spend')
plt.ylabel('Sales')
plt.show()

# 3. Boxplot comparing drug effectiveness across different age groups
plt.figure(figsize=(10, 6))
sns.boxplot(x='Age_Group', y='Effectiveness', data=df)
plt.title('Drug Effectiveness across Different Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Effectiveness')
plt.show()

# 4. Line plot showing the sales trend for each product over different trial periods
plt.figure(figsize=(10, 6))
sns.lineplot(x='Trial_Period', y='Sales', hue='Product', data=df)
plt.title('Sales Trend for Each Product over Different Trial Periods')
plt.xlabel('Trial Period')
plt.ylabel('Sales')
plt.show()

# 5. Heatmap of the correlation between Sales, Marketing_Spend, and Effectiveness
correlation_matrix = df[['Sales', 'Marketing_Spend', 'Effectiveness']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation between Sales, Marketing Spend, and Effectiveness')
plt.show()

