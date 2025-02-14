#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


City_Names = ["Toronto", "Chicago", "Houston", "Phoenix", "Philadelphia"]


# In[3]:


Population_in_millions = [6, 5, 8, 3, 2]


# In[4]:


fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (10, 4))
fig.suptitle("City Population", fontsize = 20)
ax1.bar(City_Names, Population_in_millions, color = "pink")
ax1.set(title = "City Populations", xlabel = "City Names", ylabel = "Millions of\nPeople")
ax2.pie(Population_in_millions, labels = City_Names)
ax2.legend()
plt.tight_layout
plt.show()


# In[ ]:





# In[ ]:




