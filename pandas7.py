#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd


# In[12]:


tips = pd.read_csv("tips.csv")


# In[13]:


tips["tip_rate"] = tips["tip"] / tips["total_bill"]


# In[14]:


print(tips.head(1))


# In[ ]:




