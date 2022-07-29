#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


andr = ['Android',250400543]
ios = ['Sistema Operativo IOS', 457890359]
win = ['Windows',123768349]


# lista con datos
lista_rrss = [andr, ios, win]

# crear dataframe a partir de listas
df_rrss=pd.DataFrame(lista_rrss, 
                     columns = ['Nombre del sistema operativo', 'Usuarios'])
df_rrss


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


plt.bar(df_rrss['Nombre del sistema operativo'], df_rrss['Usuarios'],
       color=['g', 'y', 'b'])
plt.show()


# In[ ]:




