#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Day_14_Pharma_data.csv')

# Perform data cleaning
# Check for missing values and handle them
print("Missing values:")
print(df.isnull().sum())

# Check for duplicates and handle them
print("\nDuplicates:")
print(df.duplicated().sum())

# Drop duplicates
df = df.drop_duplicates()



# In[8]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Day_14_Pharma_data.csv')

# Create the bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x='Region', y='Effectiveness', hue='Product', data=df)
plt.title('Average Effectiveness for Each Drug Across Different Regions')
plt.xlabel('Region')
plt.ylabel('Average Effectiveness')
plt.legend(title='Product')
plt.show()


# In[7]:



plt.figure(figsize=(12, 6))
sns.violinplot(x='Product', y='Effectiveness', data=df, inner=None, color='skyblue')
sns.violinplot(x='Product', y='Side_Effects', data=df, inner=None, color='lightgreen', alpha=0.5)
plt.title('Distribution of Effectiveness and Side Effects for Each Product')
plt.xlabel('Product')
plt.ylabel('Values')
plt.show()



# In[6]:



sns.pairplot(df, vars=['Effectiveness', 'Side_Effects', 'Marketing_Spend'], hue='Product')
plt.show()



# In[5]:



plt.figure(figsize=(12, 6))
sns.boxplot(x='Trial_Period', y='Effectiveness', data=df)
plt.title('Effectiveness for Different Trial Periods')
plt.xlabel('Trial Period')
plt.ylabel('Effectiveness')
plt.show()




# In[4]:




plt.figure(figsize=(12, 6))
sns.regplot(x='Marketing_Spend', y='Effectiveness', data=df, scatter_kws={'s': 50})
plt.title('Impact of Marketing Spend on Drug Effectiveness')
plt.xlabel('Marketing Spend')
plt.ylabel('Effectiveness')
plt.show()

