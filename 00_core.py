#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# default_exp core


# In[12]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# # jaguar
# 
# > Project the financial impact of fare changes.

# In[3]:


#hide
from nbdev.showdoc import *


# In[6]:


#export
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'


# In[7]:


say_hello("Sylvain")


# In[8]:


assert say_hello("Jeremy")=="Hello Jeremy!"


# In[9]:


#export
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to): self.to = to

    def say(self):
        "Do the saying"
        return say_hello(self.to)


# In[10]:


show_doc(HelloSayer.say)


# In[11]:


o = HelloSayer("Alexis")
o.say()


# In[ ]:





# In[13]:


from nbdev.export import notebook2script; notebook2script()


# In[ ]:




