#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


from numpy import random


# In[7]:


data = np.random.randint(10, size=(5))


# In[8]:


print(data)


# In[9]:


data2 = data.reshape(5, 1)


# In[10]:


print(data2)


# In[ ]:




