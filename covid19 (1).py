#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


df1 = pd.read_csv("https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv" , sep=",")


# In[19]:


df1.head()


# In[16]:


df1.tail()


# In[17]:


df1.shape


# In[20]:


df1


# In[8]:


df1.dtypes


# In[21]:


df1.describe(include="all").round(2)


# In[22]:


pd.set_option('display.max_columns',None)
df1.describe(include="all").round(2)


# In[23]:


df1.info()


# In[24]:


df1["location"].nunique()


# In[25]:


df1["continent"].value_counts()


# In[26]:


df1["total_cases"].mean()


# In[27]:


df1["total_cases"].max()


# In[28]:


df1["total_deaths"].describe().round(3)


# In[29]:


df1.groupby("continent").agg({"human_development_index":"max"}).head(1)


# In[30]:


df1.groupby("continent").agg({"gdp_per_capita":"min"}).head(1)


# In[31]:


df1.groupby("continent").agg({"gdp_per_capita":"min"})


# In[32]:


df1=df1[['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']]


# In[33]:


df1


# In[34]:


df1.duplicated().sum()


# In[35]:


df1.drop_duplicates()


# In[36]:


df1.isnull().sum()


# In[37]:


df1.dropna(subset=["continent"])


# In[38]:


df1 = df1.fillna(0)


# In[39]:


df1.isnull().sum()


# In[42]:


df1["date"]=pd.to_datetime(df1["date"])


# In[43]:


df1.dtypes


# In[44]:


df1["month"] = pd.DatetimeIndex(df1["date"]).month


# In[45]:


df1


# In[46]:


df1.groupby("continent").max().reset_index()


# In[47]:


df_groupby=df1.groupby("continent").max().reset_index()


# In[48]:


df_groupby


# In[49]:


df_groupby["total_deaths_to_total_cases"]=df_groupby["total_deaths"]/df_groupby["total_cases"]


# In[63]:


df_groupby["total_deaths_to_total_cases"]*100


# In[68]:


sns.displot(df1["gdp_per_capita"])
plt.show()


# In[67]:


sns.jointplot(data=df_groupby,x='total_cases',y='gdp_per_capita',kind='scatter')
plt.show()


# In[70]:


sns.pairplot(data=df_groupby)
plt.show()


# In[75]:


sns.catplot(data=df_groupby,x='continent',y='total_cases',kind='bar')
plt.show()


# In[76]:


df1.to_csv("covid_Data.csv")


# In[ ]:




