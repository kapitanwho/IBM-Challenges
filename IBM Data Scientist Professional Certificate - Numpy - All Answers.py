#!/usr/bin/env python
# coding: utf-8

# In[9]:


import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


u = np.array([1, 0])
v = np.array([0, 1])

print(u-v)


# In[4]:


z = np.array([2, 4])

print(z*-2)


# In[5]:


a = np.array([1,2,3,4,5])
b = np.array([1,0,1,0,1])

print(a)
print(b)
print(a*b)


# In[7]:


# Plotting functions

def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


# In[11]:


a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print(np.dot(a,b))


# In[12]:


a = np.array([1,0]) 
b = np.array([0,1])
Plotvec2(a,b)
print(np.dot(a,b))


# In[13]:


a = np.array([1,1]) 
b = np.array([0,1])
Plotvec2(a,b)
print(np.dot(a,b))


# In[ ]:




