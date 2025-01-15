import pandas as pd
import plotly.express as px

tabela = pd.read_csv("Arquivos/cancelamentos.csv")

tabela = tabela.drop(columns="CustomerID", axis=1)
tabela = tabela.dropna()

print(tabela)

print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

#Criando o grafico

for coluna in tabela.columns:
  grafico = px.histogram(tabela, x = coluna, color = "cancelou", title = "Cancelamentos", text_auto = True)
  #Mostrando o grafico
  grafico.show()

