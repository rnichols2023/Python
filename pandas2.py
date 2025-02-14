#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


tips = pd.read_csv("tips.csv")


# In[3]:


print(tips)


# In[4]:


bill_tip = tips.drop(columns = ["sex" , "smoker" , "day" , "time" , "size"])


# In[5]:


bill_tip


# In[ ]:




