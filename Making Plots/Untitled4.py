#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('/Users/new/Desktop/python datasets/player-stats (2).csv')
df.head()


# In[16]:


fig, ax = plt.subplots()
fig.set_size_inches(14,5)
ax = sns.violinplot(x='Team', y='Appearances', data=df)
plt.xticks(rotation=65)
ax.set_facecolor('grey')
plt.show()


# In[17]:


CSLcols = ('red','yellow','green','blue','magenta','black','purple','white','yellow','blue','red','yellow','green','blue','magenta','black','purple','white','yellow','blue','red','yellow','green')
CSLpalette = sns.color_palette(CSLcols)
fig, ax = plt.subplots()
fig.set_size_inches(16,10)
ax = sns.violinplot(x='Team', y='Appearances', data=df,palette=CSLpalette)
plt.xticks(rotation=65)
plt.show()



# In[ ]:




