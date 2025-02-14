#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


y = [1, 2, 3, 4, 5]


# In[3]:


x = [0, 1, 2, 3, 4]


# In[4]:


fig, ax = plt.subplots(figsize = (10, 10))
ax.plot(x, y)
ax.set(title = "Simple Line Chart", xlabel = "x", ylabel = "y")
plt.show()


# In[ ]:




