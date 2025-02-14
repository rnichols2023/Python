#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np


# In[15]:


arr1 = np.array([[[6, 7, 9, 2], [5, 12, 2, 10], [14, 10, 13, 15]],  [[3, 6, 5, 4], [14, 9, 8, 13], [7, 11, 1, 12]]])


# In[16]:


print(arr1)


# In[25]:


arr3 = np.array(arr1[0: , 0, 0:3])


# In[26]:


print(arr3)


# In[27]:


arr2 = arr3.reshape(2, 1 , 3)


# In[28]:


print(arr2)


# In[ ]:




