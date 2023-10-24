#!/usr/bin/env python
# coding: utf-8

# # EDA in Pandas

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"G:\Data Science\Tutorials\Pandas\Data Files\world_population.csv")
df


# In[20]:


# to display numbers upto 2 decimal
#pd.set_option('display.float_format', lambda x: f'{x:.2f}')
# OR
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df


# In[13]:


df.info()


# In[16]:


df.describe()


# In[24]:


# counting of null values
df.isnull().sum()


# In[25]:


# counting of unique values
df.nunique()


# In[30]:


# Sorting on values
df.sort_values(by="2022 Population", ascending = False).head(10)


# In[34]:


# correlation between columns
df.corr(numeric_only = True)


# In[45]:


# heatmap using seaborn
sns.heatmap(df.corr(numeric_only = True), annot = True)

plt.rcParams['figure.figsize'] = (16,10)
plt.show()


# In[53]:


# Grouping data
df.groupby('Continent').mean(numeric_only = True).sort_values(by = '2022 Population', ascending = False)


# In[52]:


df[df['Continent'].str.contains('Oceania')]


# In[59]:


df.columns


# In[65]:


# Grouping data
df2 = df.groupby('Continent')['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population'].mean(numeric_only = True).sort_values(by = '2022 Population', ascending = False)
df2


# In[66]:


df3 = df2.transpose()
df3


# In[67]:


df3.plot()


# In[82]:


# Boxplots for outliers
df.boxplot(figsize=(24,12))


# In[83]:


df.dtypes


# In[88]:


df.select_dtypes(include = 'number')


# In[ ]:




