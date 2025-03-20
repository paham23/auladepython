import pandas as pd

# 1. Criando um arquivo CSV fictício
dados = """Produto,Quantidade,Preço
Shampoo Tucumã,10,25.00
Condicionador Cupuaçu,5,30.00
Sabonete Açaí,15,12.00
Óleo de Andiroba,8,40.00
Manteiga de Murumuru,6,35.00
"""

# Salvando o CSV
with open("vendas.csv", "w", encoding="utf-8") as f:
    f.write(dados)

# 2. Lendo o arquivo CSV
df = pd.read_csv("vendas.csv")

# 3. Calculando o total vendido por produto
df["Total"] = df["Quantidade"] * df["Preço"]
total_vendas = df.groupby("Produto")["Total"].sum()

# 4. Identificando o produto mais vendido
produto_mais_vendido = total_vendas.idxmax()
valor_mais_vendido = total_vendas.max()

# 5. Exibindo o relatório
print("\n Relatório de Vendas:")
print(total_vendas)
print(f"\n Produto mais vendido: {produto_mais_vendido} (Total: R$ {valor_mais_vendido:.2f})")



