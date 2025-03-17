import pandas as pd 
dadosProdutos = pd.read_csv("analise.csv")
print(dadosProdutos.columns)

dadosProdutos ["maior produtividade"].max()
print("menor uso de agua",dadosProdutos["maior produtividade"].mean())

import pandas as pd
import matplotlib.pyplot as plt

dados_produtos = pd.read_csv('analise.csv', delimiter=',')
plt.figure(figsize=(10, 6))
for produto in dados_produtos[""]