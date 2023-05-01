#!/usr/bin/env python
# coding: utf-8

# # URL SHORTENER

# In[1]:


get_ipython().system('pip install pyshorteners')


# In[3]:


import pyshorteners
url=input("Enter the URL: ")

def shortenurl(url):
    s=pyshorteners.Shortener()
    print(s.tinyurl.short(url))
    
shortenurl(url)


# 
