#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


tips = pd.read_csv("tips.csv")


# In[3]:


print(tips)


# In[10]:


female_number = tips.set_index(["sex"])


# In[11]:


female_num = female_number.loc[("Female")].sum


# In[12]:


print(female_num)


# In[13]:


female_num = 87


# In[ ]:




