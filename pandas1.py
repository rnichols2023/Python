#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


l = [4, 8, 15, 16, 23, 42]


# In[3]:


s = pd.Series(l)


# In[5]:


print(s)


# In[14]:


s = pd.Series(l, index = ["a" , "b" , "c" , "d" , "e", "f"])


# In[15]:


print(s)


# In[ ]:




