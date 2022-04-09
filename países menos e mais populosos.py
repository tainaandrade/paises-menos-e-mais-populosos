#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 

import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rc('figure', figsize = (20, 10))

import warnings
warnings.filterwarnings("ignore")


# In[3]:


dados = pd.read_csv('dados/world_population.csv')


# In[4]:


dados


# ## Renomeando nome da coluna

# In[5]:


dados.rename(columns={'Population (2020)':'Population'}, inplace=True)


# ## Listando países mais populosos (> cem milhões)

# In[6]:


size_cem_milhoes = dados['Population'] > 100000000
paises_populosos = dados[size_cem_milhoes].sort_values(by='Population', ascending=False)


# In[7]:


paises_populosos.index = range(paises_populosos.shape[0])


# In[8]:


paises_populosos


# In[81]:


fig = plt.figure()
fig, ax = plt.subplots(figsize=(20,10))
ax.axhline(color='grey', linewidth=0.8)
ax.set_title('Países mais populosos (TOP 10)',fontsize= 22)

ax.set_ylabel('Tamanho da População', fontsize=20)
ax.set_xlabel('Nome dos Países', fontsize=20)
country = paises_populosos['Country/Other'].head(10)
population = paises_populosos['Population'].head(10)


plt.gca().set_yticklabels(['{:}'.format(x) for x in population])


plt.yticks(population)
ax.bar(country, population)


plt.show()


# ## Listando países menos populosos (< cem milhões)

# In[10]:


size_menos_cem_milhoes = dados['Population'] < 100000000
paises_nao_populosos = dados[size_menos_cem_milhoes].sort_values(by='Population', ascending=True)


# In[53]:


paises_nao_populosos.index = range(paises_nao_populosos.shape[0])


# In[82]:


paises_nao_populosos


# 

# In[80]:


fig = plt.figure()

fig, ax = plt.subplots(figsize=(20,10))
ax.axhline(color='grey', linewidth=0.8)
ax.set_title('Países menos populosos (TOP 10)',fontsize= 22)

       




ax.set_ylabel('Tamanho da População', fontsize=20)
ax.set_xlabel('Nome dos Países', fontsize=20)
country = paises_nao_populosos['Country/Other'].head(10)
population = paises_nao_populosos['Population'].head(10)


plt.gca().set_yticklabels(['{:}'.format(x) for x in population])


plt.yticks(population)
ax.bar(country, population)


plt.show()


# In[ ]:




