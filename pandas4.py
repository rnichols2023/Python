#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


tips = pd.read_csv("tips.csv")


# In[3]:


print(tips)


# In[9]:


tips_50 = tips.loc[50]


# In[10]:


print(tips_50)


# In[ ]:




