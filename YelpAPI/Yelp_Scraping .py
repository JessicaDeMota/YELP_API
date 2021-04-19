#!/usr/bin/env python
# coding: utf-8

# In[117]:


from bs4 import BeautifulSoup 


# In[118]:


import requests 


# In[119]:


page = requests.get('https://www.yelp.com/biz/blue-ribbon-fried-chicken-east-village-new-york-2?osq=Blue+Ribbon+Restaurant')


# In[120]:


page.status_code 


# In[121]:


page.text


# In[122]:


soup = BeautifulSoup(page.text, 'html.parser')


# In[123]:


results = soup.findAll(class_='lemon--span__373c0__3997G raw__373c0__3rKqk', attrs={'lang':'en'})


# In[124]:


reviews = [result.text for result in results]


# In[125]:


print (reviews)


# In[126]:


import pandas as pd 
import numpy as np 


# In[127]:


df = pd.DataFrame(np.array(reviews), columns = ['review'])


# In[128]:


df.head()


# In[129]:


len(df['review'])


# In[130]:


df['word count'] = df['review'].apply(lambda x: len(x.split()))


# In[131]:


df.head()


# In[132]:


len(df['review'])


# In[133]:


df['char_count'] = df['review'].apply(lambda x:len(x))


# In[134]:


def average_words(x):
   words = x.split()
   return sum(len(word)for word in words) / len(words)


# In[143]:


df['average_word_length'] = df['review'].apply(lambda x: average_words(x))


# In[144]:


df.head()


# In[151]:


import nltk


# In[152]:


nltk.download('stopwords')


# In[158]:


from nltk.corpus import stopwords 


# In[159]:


stop_words = stopwords.words('english')


# In[160]:


len(stop_words)


# In[168]:


df['review'].apply(lambda.x: len([word for word in x.split() if word.lower() in stop_words ]))


# In[ ]:





# In[ ]:




