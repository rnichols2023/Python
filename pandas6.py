#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd


# In[57]:


data = pd.read_csv("tips.csv")


# In[62]:


data = data.rename(columns = {"sex" : "gender"})


# In[63]:


print(data)


# In[ ]:




