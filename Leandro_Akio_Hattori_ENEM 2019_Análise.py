#!/usr/bin/env python
# coding: utf-8

# #Análise exploratório do rsultado do Enem 2019##

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
source = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"
data = pd.read_csv(source)
data.head()
#data = pd.read_csv("C:/Users/Leandro Akio Hattori/Desktop/Estudos/Enem 2019/MICRODADOS_ENEM_2019.csv",encoding = "ISO-8859-1", sep = ';')#


# In[10]:


data.head(3)


# In[11]:


##Análise 1 - Proporção de inscritos por idade / Application by age##
data["NU_IDADE"].value_counts(normalize=True).sort_index()*100


# In[17]:


##Análise 2 - Descobrir de quais estados são os inscritos com 13 anos##
data.query("NU_IDADE == 13")["SG_UF_RESIDENCIA"].unique()
data.query("NU_IDADE == 13")["SG_UF_RESIDENCIA"].value_counts()


# In[18]:


##Análise 3 - Adicionar título no gráfico##
import matplotlib as plt
data["NU_IDADE"].plot.hist(bins = 40, figsize=(8, 6), title="Distribuição de inscritos no Enem por idade", grid=True)


# In[19]:


##Análise 4: Plotar os histogramas das idades dos treineiro e não treineiros##
import matplotlib.pyplot as plt
data.query("IN_TREINEIRO == 1")["NU_IDADE"].hist(bins=40, color = 'orange',alpha =0.5, figsize=(8,6), grid=True)
data.query("IN_TREINEIRO != 1")["NU_IDADE"].hist(bins=40, color = 'blue', alpha =0.5, figsize=(8,6), grid=True)
plt.title(" ENEM 2019 - Histograma das idades dos inscritos treineiros e não-treineiros")
plt.legend(['Treineiro', 'Não-Treineiro'])
plt.xlabel('idade')
plt.ylabel('nº de inscrições')
#A maioria dos treineiros possuem aproximadamente entre 15 e 17 anos#


# In[20]:


##Análise 5 : Comparar as distribuições das provas de matemática em inglês espanhol##
provas = ["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_MT","NU_NOTA_LC","NU_NOTA_REDACAO"]
data.query("TP_LINGUA == 0")["NU_NOTA_MT"].hist(bins=50, alpha=0.5) 
plt.title('Histogramas de notas de Matemática - INGLÊS (azul) - ESPANHOL (laranja)')
data.query("TP_LINGUA == 1")["NU_NOTA_MT"].hist(bins=50, alpha=0.5)
#na escolha da língua estrangeira, houve maior número de alunos que escolheram Ingles#


# In[21]:


data["SG_UF_RESIDENCIA"]


# In[22]:


#Exibir gráfico com distribuição percentual de candidatos menores de 14 anos por estado#
alunos_menor14 = data.query("NU_IDADE <= 14")
alunos_menor14["SG_UF_RESIDENCIA"].value_counts(normalize=True).plot.barh(figsize = (5,5))


# In[23]:


#visualização da distribuição das notas de Matemática por renda familiar dos candidatos#
renda_ordenada = data["Q006"].unique()
renda_ordenada.sort()
renda_ordenada
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(14,6))
sns.boxplot(x="Q006", y="NU_NOTA_MT", data = data, order = renda_ordenada)
plt.title("Distribuição de notas de matemática por renda")
#quanto maior a renda, maiores são as quantidades de notas mais altas, pois no geral têm condições de se dedicarem mais tempo aos estudos)


# In[ ]:




