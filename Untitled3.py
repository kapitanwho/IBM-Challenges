#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

a = np.array(a)


# In[5]:


a.size


# In[6]:


a[0][0:2]


# In[8]:


B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])

C = np.dot(a,B)
print(C)


# In[ ]:




