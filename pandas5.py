#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd


# In[23]:


tips = pd.read_csv("tips.csv")


# In[27]:


tips_7 = tips.iloc[7]['total_bill']


# In[28]:


print(tips_7)


# In[ ]:




