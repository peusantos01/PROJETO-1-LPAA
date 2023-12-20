
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from subprocess import check_output

###lendo arquivo csv que ira ser tratado
df = pd.read_csv('/content/Health_AnimalBites.csv', sep=',')

###exibindo 10 primeiras linhas do dataframe para ter uma nocao do que se trata os dados
print(df.head(10))

###sabendo do que se trata o dataframe, realizaremos um estudo de casos
###definindo quem é a coluna de data
coluna_de_data = 'bite_date'
###primeiramente limparemos as linhas que nao tiverem datas registros, pois para o estudo so consideramos com data
###além disso, removeremos linhas duplicatas
df_limpo = df.drop_duplicates().dropna(subset=[coluna_de_data])
###exibindo dataframe após remoção das linhas sem data
print(df_limpo)

###agora temos a curiosidade de descobrir qual animal que mais mordeu durante todo o período do estudo
###definindo a coluna de animais
coluna_de_animal = 'SpeciesIDDesc'
animal_que_mais_mordeu = df_limpo[coluna_de_animal].mode().iloc[0]

###resultado do animal que mais mordeu
print(f"O animal que mais mordeu durante o período do estudo foi {animal_que_mais_mordeu}")

###que tal jogarmos isso num grafico de barras azul?

###contando a quantidade de vezes que certo animal mordeu durante o periodo do estudo

contagem_animal = df_limpo[coluna_de_animal].value_counts()

###plotando o grafico requerido
contagem_animal.plot(kind='bar',color='blue')
plt.title(f'Quantidade de mordidas por animal durante o estudo')
plt.xlabel('Animal')
plt.ylabel('Quantidade')
plt.show()


###fazendo outro grafico, agora de quantas vezes um certo animal mordeu tal gênero
#definindo qual coluna de genero
coluna_de_genero = 'GenderIDDesc'
contagem_ocorrencias = df.groupby([coluna_de_animal,coluna_de_genero]).size().reset_index(name='Contage')

##criando grafico
plt.figure(figsize=(25,28))
plt.bar(contagem_ocorrencias[coluna_de_animal] + ' - ' + contagem_ocorrencias[coluna_de_genero], contagem_ocorrencias['Contage'])
plt.title('Quantidade de vezes que cada animal mordeu por genero')
plt.xlabel('Animal - Sexo')
plt.ylabel('Contage')
plt.show()

