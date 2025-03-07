#!/usr/bin/env python
# coding: utf-8

# # WALMART SALES ANALYSIS PROJECT
# 
# ## DATA CLEANING AND PREPROCESSING
# 

# In[38]:


pip install pymysql


# In[39]:


pip install sqlalchemy


# In[40]:


pip install pandas


# In[45]:


# IMPORTING THE LIBRARIES

import pandas as pd

#importing mysql toolkit
import pymysql
from sqlalchemy import create_engine

df = pd.read_csv("C:/Users/HP/Desktop/project_walmart/walmart-10k-sales-datasets/Walmart.csv")

df.shape
df.head


# In[10]:


df.head()


# In[11]:


df.describe()


# In[12]:


df.info()


# In[13]:


#all duplicates
df.duplicated().sum()


# In[17]:


#removing duplicates
df.drop_duplicates(inplace=True)
df.duplicated().sum()


# In[19]:


#the number of columns have decreased after removing duplicates
df.shape


# In[14]:


#missing values
df.isnull().sum()


# In[20]:


#dropping all rows with missing records
df.dropna(inplace = True)


# In[21]:


#checking whether all null values are dropped
df.isnull().sum()


# In[23]:


#number of rows have decreased
df.shape


# In[72]:


#converting the unit_price into float value
df['unit_price'] = df['unit_price'].astype(str).str.replace('$', '', regex=False).astype(float)
df.head()


# In[73]:


#checking if the data type of unit_price has been converted to float or not
df.info()


# In[36]:


#shows all the columns in the data set
df.columns


# In[74]:


#creating a new column total
df['total'] = df['unit_price'] * df['quantity']
df.head()


# ## establishing connection with mysql

# In[53]:


#login requirements for mysql
host = "127.0.0.1"
port = "3306"
user = "root"
password = "12345"
print("Connected successfully!")


# In[75]:


df.shape


# In[76]:


df.to_csv('walmart_clean_data.csv', index = False)


# In[56]:


help (create_engine)


# In[77]:


#mysql connection
# mysql+pymysql://scott:tiger@hostname/dbname"
engine_mysql = create_engine("mysql+pymysql://root:12345@localhost:3306/walmart_db")
try:
    engine_mysql
    print("connection successfull")
except:
    print("unable to connect")
                             


# In[108]:


#exporting dataset to sql
df.to_sql(name='walmart2', con=engine_mysql, if_exists='fail', index=False)


# In[87]:


df.shape


# In[88]:


df.to_csv('walmart_clean_data.csv', index=False)


# In[91]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Load the dataset

df = pd.read_csv("C:/Users/HP/Desktop/project_walmart/walmart-10k-sales-datasets/Walmart.csv")
# Display first few rows
print(df.head())


# In[92]:


# Total records count
total_records = len(df)
print(f"Total records: {total_records}")


# In[93]:


# Count payment methods and number of transactions by payment method
payment_counts = df.groupby("payment_method").size().reset_index(name="no_payments")
print(payment_counts)


# In[95]:


# Visualization: Number of Transactions by Payment Method
plt.figure(figsize=(8, 5))
sns.barplot(x="payment_method", y="no_payments", data=payment_counts, palette="viridis")
plt.title("Number of Transactions by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.show()


# In[97]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you fetched the data from the database and stored it in a DataFrame
highest_rated = pd.DataFrame({
    'branch': ['A', 'B', 'C'],  # Replace with actual branch names
    'category': ['Electronics', 'Grocery', 'Clothing'],  # Replace with actual category names
    'avg_rating': [4.8, 4.6, 4.7]  # Replace with actual ratings
})

# Visualization: Highest-Rated Categories
plt.figure(figsize=(10, 5))
sns.barplot(x="branch", y="avg_rating", hue="category", data=highest_rated, palette="coolwarm")
plt.title("Highest-Rated Category per Branch")
plt.xlabel("Branch")
plt.ylabel("Average Rating")
plt.legend(title="Category")
plt.show()


# In[ ]:




