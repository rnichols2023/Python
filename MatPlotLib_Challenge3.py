#!/usr/bin/env python
# coding: utf-8

# In[14]:


import seaborn as sns


# In[15]:


import matplotlib.pyplot as plt


# In[16]:


iris = sns.load_dataset("iris")


# In[17]:


iris.head()


# In[19]:


fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (10,4))
fig.suptitle("Iris Dataset Visualizations", fontsize = 14)
sns.histplot(data = iris, x = "petal_length", ax = ax1)
ax1.set_title("Distribution of Petal Lengths")
ax1.set(xlabel = "Petal Length", ylabel = "Count")
sns.boxplot(data = iris, x = "species", y = "sepal_length", ax = ax2)
ax2.set_title("Sepel Length By Species")
ax2.set(xlabel = "Species", ylabel = "Sepel Length")
plt.tight_layout()
plt.show()


# In[ ]:




