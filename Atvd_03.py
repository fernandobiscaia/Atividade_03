#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import json
import seaborn as sns
import matplotlib.pyplot as plt
from operator import itemgetter, attrgetter

#URL relacao de emresas brasileiras habilitadas para a ligacao Brasil Peru
url = 'https://dados.antt.gov.br/dataset/f22f6b08-4050-4dad-8a93-bc68826629d4/resource/01cbd874-2b38-4053-81cd-0aedf63fe193/download/empresas_brasil_peru.json'

#Criacao dataframe
df = pd.DataFrame()
r = requests.get(url).json()
df = pd.json_normalize(r['empresas_brasil_peru'])

#Filtrando as variaveis necessarias
df=df[['razao_social', 'total_de_veiculos']]
#Transformando a variavel total_de_veiculos em numerica
df['total_de_veiculos'] = df['total_de_veiculos'].astype(int)
#ordenando a variavel total_de_veiculos em ordem decrescente
df_ord = df.sort_values(by=['total_de_veiculos'], ascending=False)
#Mantendo somente as 10 empresas com maior numero de veiculos
df_drop = df_ord.iloc[:10]

#criando grafico de barras das 10 empresas com maior numero de veiculos
fig, ax = plt.subplots()
sns.barplot(x='total_de_veiculos', y='razao_social', data=df_drop, order=df_drop.groupby(["razao_social"])["total_de_veiculos"].mean().sort_values(ascending=False).index)
fig.tight_layout();


# In[ ]:




