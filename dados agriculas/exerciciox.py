import pandas as pd
import matplotlib.pyplot as plt
#carregando dados
dados_produtos = pd.read_csv('produtos.csv' ,delimiter=';')

#criando o grafico de PRECO por ANO para cada PRODUTO
plt.figure(figsize=(10, 6))

#Plotando os dados para cada produto 
for produto in dados_produtos('produto').unique():
    dados_produto = dados_produtos[dados_produtos['produto']==]
    plt.plot(dados_produto['ano'], dados_produto['preco'], label=produto, marker='o')

    #adicionando titulo e rotulos 
    plt.title('preco dos produtos ao longo dos anos')
    plt.xlabel('ano')
    plt.ylabel('preco')
    plt.legend(title='produto')

    #exibindo o grafico
    plt.grid(true)
    plt.show()
