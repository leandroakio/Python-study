#!/usr/bin/env python
# coding: utf-8

# ##Análise 1 - Proporção de inscritos por idade / Application by age##

# In[2]:


import pandas as pd
fonte = "C:/Users/Leandro Akio Hattori/Desktop/Estudos/Enem 2019/MICRODADOS_ENEM_2019_SAMPLE_43278.csv"
dados = pd.read_csv(fonte)
dados.head()


# In[4]:


dados["NU_IDADE"].value_counts().sort_index()


# In[16]:


dados["NU_IDADE"].value_counts(normalize=True).sort_index()*100


# In[29]:


##Análise 2 - Descobrir de quais estados são os inscritos com 13 anos##
dados.query("NU_IDADE == 13")["SG_UF_RESIDENCIA"].unique()
#contando alunos por estado: dados.query("NU_IDADE == 13")["SG_UF_RESIDENCIA"].unique()#


# In[35]:


##Análise 3 - Adicionar título no gráfico##
import matplotlib as plt
dados["NU_IDADE"].plot.hist(bins = 20, figsize=(8, 6), title="Distribuição de inscritos no Enem por idade", grid=True)


# In[65]:


##Análise 4: Plotar os histogramas das idades dos treineiro e não treineiros##
import matplotlib.pyplot as plt
dados.query("IN_TREINEIRO == 1")["NU_IDADE"].hist(bins=20, color = 'orange', figsize=(8,6), grid=True)
dados.query("IN_TREINEIRO != 1")["NU_IDADE"].hist(bins=20, color = 'blue', figsize=(8,6), grid=True)
plt.title(" ENEM 2019 - Histograma das idades dos inscritos treineiros e não-treineiros")
plt.legend(['Treineiro', 'Não-Treineiro'])
plt.xlabel('idade')
plt.ylabel('nº de inscrições')


# In[71]:


##Análise 5 : Comparar as distribuições das provas de matemática em inglês espanhol##
import matplotlib.pyplot as plt
provas = ["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_MT","NU_NOTA_LC","NU_NOTA_REDACAO"]
dados.query("TP_LINGUA == 0")["NU_NOTA_MT"].hist(bins=50) 
plt.title('Histogramas de notas de Matemática - INGLÊS (azul) - ESPANHOL (laranja)')
dados.query("TP_LINGUA == 1")["NU_NOTA_MT"].hist(bins=50)


# In[ ]:




