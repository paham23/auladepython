import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Ler o arquivo CSV
df = pd.read_csv("vendas.csv")

# 2. Calcular a quantidade total vendida por produto
quantidade_vendas = df.groupby("Produto")["Quantidade"].sum().reset_index()

# 3. Criar o gráfico de barras
plt.figure(figsize=(10, 5))
sns.barplot(x="Quantidade", y="Produto", data=quantidade_vendas, palette="viridis")

# 4. Adicionar rótulos
plt.xlabel("Quantidade Vendida")
plt.ylabel("Produto")
plt.title("Quantidade Vendida por Produto")
plt.grid(axis="x", linestyle="--", alpha=0.7)

# 5. Salvar o gráfico como imagem
plt.savefig("grafico.png", dpi=300, bbox_inches="tight")
plt.show()

print("Gráfico salvo como 'grafico.png'")
