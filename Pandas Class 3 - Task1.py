#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1. Read this dataset in pandas,mysql and mongodb


# In[ ]:


# read dataset in pandas


# In[5]:


import pandas as pd


# In[6]:


df = pd.read_csv('FitBit data.csv')


# In[50]:


df.head()


# In[ ]:


# # While creating a data in mysql don't use manual approach to create it, always use a automation to create a table in mysql


# In[53]:


import mysql.connector as conn

mydb  = conn.connect(host = "localhost",user = "root",passwd = "data@scientist21#*",database="FitBit1_track")
print(mydb)


# In[56]:


data = pd.read_sql_query("""select * from Fitbit_Data""",mydb)


# In[57]:


data.head()


# In[ ]:


# read data from mongodb


# In[3]:


import pymongo as pymongo


# In[4]:



client = pymongo.MongoClient("mongodb+srv://Sonali:datascientist@cluster0.u4r6hcl.mongodb.net/?retryWrites=true&w=majority")
database = client['csvconverter']
collection = database['data']
x = collection.find()
for data in x:
    print(x)


# In[9]:


# Convert all the data available in dataset to timestamp format in pandas and in sql convert it into date format


# In[10]:


df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])


# In[13]:


type(df['ActivityDate'][0])


# In[14]:


df.head()


# In[15]:


# Find out in this data how many unique id we have


# In[17]:


df['Id'].nunique()


# In[18]:


# Which id is one of the most active id that you have in whole dataset


# In[25]:


df.groupby('Id')['VeryActiveMinutes'].sum().idxmax()


# In[26]:


# How many of them have not logged there activity find out in terms of number of ids


# In[28]:


df.groupby('Id')['LoggedActivitiesDistance'].sum()<1


# In[29]:


# Find out who is the laziest person id that we have in the dataset


# In[30]:


df.groupby('Id')['VeryActiveMinutes'].sum().idxmin()


# In[31]:


#  Explore over an internet that how much calories burnt is required for a healthy person and find out how many healthy person 
#  we have in our dataset (2200 calories/day)


# In[38]:


df.groupby('Id')['Calories'].sum().apply(lambda x:x>2200*7).value_counts()


# In[39]:


# How many persons are not a regular with respect to activit try to find out those


# In[41]:


df[df['TotalSteps']==0]


# In[42]:


# Who is the third most active person in this dataset find out those in pandas  


# In[43]:


df.groupby('Id')['VeryActiveMinutes'].sum().sort_values(ascending=False)[2:3]


# In[44]:


# Who is the fifth most laziest person available in dataset find it out


# In[45]:


df.groupby('Id')['VeryActiveMinutes'].sum().sort_values()[4:5]


# In[46]:


# What is the total cummulative calories burn for a perso find out


# In[47]:


df.groupby('Id')["Calories"].sum()


# In[ ]:




