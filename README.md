# Previsão de Vendas com IA
IA que prevê as vendas baseado na base de dados de uma empresa fictícia.

## Sobre o Projeto
<p># Créditos Lira Hashtag</p>

O desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos
em anúncios nas 3 grandes redes que em uma empresa fictícia que investe em: TV, Jornal e Rádio.

**Obs:** Na tabela o investimento estão em milhares de reais, e as vendas em milhões.

Nesse Projeto foi utilizado:
- A lib **pandas** -> Para Análise e Tratamento de Dados

  - ```Python
    # Importando Base de Dados
    tabela = pd.read_csv('publicidade.csv')
  
- A lib **seaborn** e a **matplotlib**-> Desenhar e Exibir os Gráficos

  - ```Python
    # Criar Grafico
              # Apresenta a Correlação entre cada um dos itens 
    sns.heatmap(tabela.corr(), cmap='Wistia', annot=True)

    # Exibir o Grafico
    plt.show()
    
- A lib **sklearn** -> Biblioteca para Machine Learning (Utilizar Modelos e Comparação entre as IAs)

  - ```Python
      # Criar uma IA
      modelo_regressaolinear = LinearRegression()
      modelo_arvoredecisao = RandomForestRegressor()

*obs*: Algumas das libs será necessário instalar, dependendo do ambiente em que esteja utilizando.
## 

### Sobre os IAs utilizados

- Regressão Linear
- Arvore de Decisão

Ambas foram treinadas:
```Python
# Treinar a IA
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)
```

Após o Teste entre as IAs:
```Python
# Avaliação entre as IAs

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste,previsao_arvoredecisao))
```

### Gráfico Comparativo

<img src="https://cdn.discordapp.com/attachments/897304698468565022/931799379533246484/Figure_1.png" width="500px">


Resultado da avaliação entre os modelos de IAs

Regressão Linear = 0.907...

Arvore de Decisão = 0.963...

Pelo resultado, a **Arvore de Decisão**, têm uma precisão melhor do que a de Regressão Linear. Logo, esse foi o modelo utilizado no final.

Após a comparação é gerado um nova base de dados, contendo a previsão de vendas:
```Python
# Adicionando nova coluna
novos['Vendas'] = previsao
print(novos)

# Exportar Nova Tabela com Previsao
novos.to_excel('Tabela com Previsao.xlsx', index=False)
```
## 

## Preview no Jupyter
https://github.com/satoosan/Criando-Primeira-IA/blob/main/Previs%C3%A3o%20de%20Vendas.ipynb
