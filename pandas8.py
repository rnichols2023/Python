#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd


# In[37]:


tips = pd.read_csv("tips.csv")


# In[38]:


over_10 = tips[tips["total_bill"] > 10]


# In[39]:


len(over_10)


# In[41]:


print(len(over_10))


# In[ ]:




