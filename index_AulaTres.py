import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Leitura dos dados
tabela = pd.read_csv("Arquivos/clientes.csv")
print(tabela)

# Codificação das colunas categóricas
codificador_profissao = LabelEncoder()
tabela["profissao"] = codificador_profissao.fit_transform(tabela["profissao"])

codificador_credito = LabelEncoder()
tabela["mix_credito"] = codificador_credito.fit_transform(tabela["mix_credito"])

codificador_pagamento = LabelEncoder()
tabela["comportamento_pagamento"] = codificador_pagamento.fit_transform(tabela["comportamento_pagamento"])

# Definindo variável target e features
y = tabela["score_credito"]
x = tabela.drop(columns=["score_credito", "id_cliente"])

# Divisão dos dados em treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=42)  

# Criação dos modelos(IA)
modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

# Treinamento dos modelos(IA)
modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

# Previsão dos dados
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

# Avaliação dos resultados => Acuracia da arvore de decisão foi de 82% e o do knn foi de 73%
print("Acuracia da arvore de decisão: ", modelo_arvoredecisao.score(x_teste, y_teste))
print("Acuracia do knn: ", modelo_knn.score(x_teste, y_teste))

# codificação nas colunas categóricas dos novos dados
tabela_novos_clientes = pd.read_csv("Arquivos/novos_clientes.csv")

tabela_novos_clientes["profissao"] = codificador_profissao.transform(tabela_novos_clientes["profissao"])
tabela_novos_clientes["mix_credito"] = codificador_credito.transform(tabela_novos_clientes["mix_credito"])
tabela_novos_clientes["comportamento_pagamento"] = codificador_pagamento.transform(tabela_novos_clientes["comportamento_pagamento"])

previsao_novos_clientes_arvoredecisao = modelo_arvoredecisao.predict(tabela_novos_clientes)
previsao_novos_clientes_knn = modelo_knn.predict(tabela_novos_clientes)

print(previsao_novos_clientes_arvoredecisao)
print(previsao_novos_clientes_knn)

