import pandas as pd
dadosProdutos = pd.read_csv("Biblioteca.csv")
print(dadosProdutos)

#analise e estatisticas com pandas






import pandas as pd


dadosProdutos = pd.read_csv("Biblioteca.csv")
dadosProdutos['preco'] .max()
print("Media de Precos dos Produtos", dadosProdutos['preco'].mean())