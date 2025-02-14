#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


tips = pd.read_csv("tips.csv")


# In[8]:


print(tips)


# In[13]:


bill_per_day = tips.groupby("day").total_bill.mean()


# In[14]:


print(bill_per_day)


# In[ ]:




