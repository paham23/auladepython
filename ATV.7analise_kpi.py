import pandas as pd 

# 1️⃣ Ler os dados do CSV
df = pd.read_csv("vendas.csv")

# 2️⃣ Converter colunas para valores numéricos (evita erros)
df["Preço"] = pd.to_numeric(df["Preço"], errors="coerce")
df["Custo"] = pd.to_numeric(df["Custo"], errors="coerce")
df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce")

# 3️⃣ Criar coluna de lucro por unidade
df["Lucro"] = df["Preço"] - df["Custo"]

# 4️⃣ Calcular o Ticket Médio (Receita Total / Total de Vendas)
receita_total = (df["Quantidade"] * df["Preço"]).sum()
total_vendas = df["Quantidade"].sum()
ticket_medio = receita_total / total_vendas

# 5️⃣ Identificar produtos com baixa margem de lucro (< 20%)
df["Margem_Lucro"] = (df["Lucro"] / df["Preço"]) * 100
produtos_baixa_margem = df[df["Margem_Lucro"] < 20]

# 6️⃣ Calcular os 3 produtos mais lucrativos
df["Lucro_Total"] = df["Lucro"] * df["Quantidade"]
top3_lucrativos = df.nlargest(3, "Lucro_Total")

# 7️⃣ Exibir os resultados
print(f"Ticket Médio: R$ {ticket_medio:.2f}")

print("\nProdutos com baixa margem de lucro (<20%):")
print(produtos_baixa_margem[["Produto", "Margem_Lucro"]])

print("\nTop 3 produtos mais lucrativos:")
print(top3_lucrativos[["Produto", "Lucro_Total"]])
