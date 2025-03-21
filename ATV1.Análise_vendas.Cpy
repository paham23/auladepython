import pandas as pd

df = pd.read_csv("vendas.csv")

df["Total"] = df["Quantidade"] * df["Preço"]
total_vendas = df.groupby("Produto")["Total"].sum()

produto_mais_vendido = total_vendas.idxmax()
valor_mais_vendido = total_vendas.max()


print("\n Relatório de Vendas:")
print(total_vendas)
print(f"\n Produto mais vendido: {produto_mais_vendido} (Total: R$ {valor_mais_vendido:.2f})")

