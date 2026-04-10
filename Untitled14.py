#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[7]:


df=pd.read_csv(r'C:\Users\Administrator\Downloads\archive\tested.csv')
df.head()


# In[8]:


df.info()


# In[9]:


df['Age']=df['Age'].fillna(df['Age'].median())


# In[10]:


df['Fare']=df['Fare'].fillna(df['Fare'].median())


# In[12]:


df=df.drop(columns=['Cabin'])


# In[13]:


df.info()


# In[19]:


print("Duplicates before:", df.duplicated().sum())


# In[20]:


df=df.drop_duplicates()


# In[21]:


print("duplicates after:", df.duplicated().sum())


# In[22]:


df['Survived']=df['Survived'].astype('category')
df['Pclass']=df['Pclass'].astype('category')
df['Sex']=df['Sex'].astype('category')
df['Embarked']=df['Embarked'].astype('category')


# In[23]:


df.dtypes


# In[24]:


df=df.rename(columns={'PassengerId': 'passenger_id',
    'Survived': 'survived',
    'Pclass': 'passenger_class',
    'Name': 'name',
    'Sex': 'sex',
    'Age': 'age',
    'SibSp': 'siblings_spouses',
    'Parch': 'parents_children',
    'Ticket': 'ticket',
    'Fare': 'fare',})


# In[25]:


df.head()


# In[27]:


df=df.rename(columns={'Embarked':'embarked'})


# In[28]:


df.head()


# In[29]:


df.to_csv('titanic_cleaned.csv', index=False)
print("clean dataset saved!")


# In[ ]:




