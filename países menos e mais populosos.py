#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 

import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rc('figure', figsize = (20, 10))

import warnings
warnings.filterwarnings("ignore")

dados = pd.read_csv('dados/world_population.csv')

dados


dados.rename(columns={'Population (2020)':'Population'}, inplace=True)


size_cem_milhoes = dados['Population'] > 100000000
paises_populosos = dados[size_cem_milhoes].sort_values(by='Population', ascending=False)



paises_populosos.index = range(paises_populosos.shape[0])


paises_populosos


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

<img src="https://user-images.githubusercontent.com/27781259/162550365-f7080772-eec5-4c6f-9889-ead75f9058c6.png">

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




