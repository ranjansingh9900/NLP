#!/usr/bin/env python
# coding: utf-8

# In[3]:


# First, make sure to install the NLTK library
# You can install it using pip if you haven't already:
get_ipython().system('pip install nltk')

import nltk
nltk.download('punkt')  # Download the necessary NLTK data files
from nltk.tokenize import word_tokenize


# In[4]:


# Example sentence
sentence = "Natural Language Processing is fascinating."


# In[5]:


# Word tokenization
tokens = word_tokenize(sentence)

# Print the tokens
print(tokens)


# In[ ]:




