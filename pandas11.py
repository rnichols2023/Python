#!/usr/bin/env python
# coding: utf-8

# In[85]:


import pandas as pd


# In[86]:


tips = pd.read_csv("tips.csv")


# In[87]:


tips_sum = tips.groupby(["day", "smoker"])["tip"].sum()


# In[88]:


print(tips_sum)


# In[ ]:




