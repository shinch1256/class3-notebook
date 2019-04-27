#!/usr/bin/env python
# coding: utf-8

# In[9]:


import  os
if os.path.isfile('wine.data'):
    print('it  is  a file')
else:
    print('no file')


# In[5]:


f=open('wine.data')


# In[8]:


for line  in  f.readlines():
    print(line)


# In[ ]:




