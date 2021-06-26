#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlp
from pywaffle import Waffle


# In[30]:


df = pd.read_csv('/Users/new/Desktop/josef yarney 2.csv')


my_list = df.columns.values.tolist()
df = pd.DataFrame(df,columns=my_list)

df.head(8)


# In[34]:


fig = plt.figure(
    FigureClass = Waffle,
    values = df.iloc[:,1],
    labels = list(df.Name),
    rows = 3,
    legend = {'loc':'upper left','bbox_to_anchor':(1,1)},
    title = {'label':'Tackles','loc':'left'},
    icons = 'futbol', icon_size = 60, icon_legend=True
    
)
background = '#313332'
fig.set_facecolor('white')


plt.show()


# In[ ]:




