# Creditos Lira Hashtag

# Previsão de Vendas
# O desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos
# em anúncios nas 3 grandes redes que em uma empresa fictícia que investe em: TV, Jornal e Rádio

# Importar a Base de Dados para
import pandas as pd
import seaborn as sns  # Criação dos Gráficos
import matplotlib.pyplot as plt  # Exibição dos Gráficos

from sklearn.model_selection import train_test_split  # Lib Machine Learning
from sklearn.linear_model import LinearRegression # Modelo Machine Learning
from sklearn.ensemble import RandomForestRegressor  # Modelo Machine Learning
from sklearn import metrics # Comparacao entre IAs

# Obs: Na tabela o investimento estão em milhares de reais, e as vendas em milhões

tabela = pd.read_csv('publicidade.csv')
print(tabela)

tabela.info()
# ------------------------------- #

# Analise Exploratória

# Criar Grafico
            # Apresenta a Correlação entre cada um dos itens
sns.heatmap(tabela.corr(), cmap='Wistia', annot=True)

# Exibir o Grafico
plt.show()
# -------------------------------- #

# Preparação dos Dados para treinar o modelo de Machine Learning

# Separar os dados em dados de treino e dados de teste
y = tabela['Vendas']  # Quem eu quero prever
x = tabela[['TV', 'Radio', 'Jornal']]  # Quem eu vou usar para fazer a previsao

# Ira pegar de forma aleatória partes da base de dados, e separa-las, em uma parte de treino e outra de teste
x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y, test_size=0.3, random_state=1)
# ------------------------------- #

# Escolher qual modelo usar

# Criar uma IA
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# Treinar a IA
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)
# ------------------------------- #

# Teste IA
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste,previsao_arvoredecisao))

# ------------------------------- #

# Visualização Gráfica das Previsões
# A arvore de decisão é o melhor modelo 

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['Previsao Regressao Linear'] = previsao_regressaolinear
tabela_auxiliar['Previsao Arvore Decisao'] = previsao_arvoredecisao

plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)
plt.show()

# ------------------------------- #

# Fazendo agora novas previsões
# importar nova tabela com as informações de propaganda em TV, Radio e Jornal
# Passa a nova tabela para o predict do seu modelo

novos = pd.read_csv('novos.csv')
print(novos)

previsao = modelo_arvoredecisao.predict(novos)
print(previsao)

# Adicionando nova coluna
novos['Vendas'] = previsao
print(novos)

# Exportar Nova Tabela com Previsao
novos.to_excel('Tabela com Previsao.xlsx', index=False)
