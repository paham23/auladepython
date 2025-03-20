import pandas as pd

# 1. Ler o arquivo CSV
df = pd.read_csv("vendas.csv")

# 2. Calcular o total vendido por produto
df["Total"] = df["Quantidade"] * df["Preço"]
total_vendas = df.groupby("Produto", as_index=False)["Total"].sum()

# 3. Identificar o produto mais vendido
produto_mais_vendido = total_vendas.loc[total_vendas["Total"].idxmax()]

# 4. Criar um arquivo Excel com duas abas: "Vendas" e "Resumo"
with pd.ExcelWriter("relatorio.xlsx", engine="openpyxl") as writer:
    # Aba 1: Todos os dados de vendas
    df.to_excel(writer, sheet_name="Vendas", index=False)
    
    # Aba 2: Resumo das vendas
    resumo_df = pd.DataFrame({
        "Produto mais vendido": [produto_mais_vendido["Produto"]],
        "Total vendido (R$)": [produto_mais_vendido["Total"]],
        "Total geral de vendas (R$)": [total_vendas["Total"].sum()]
    })
    
    total_vendas.to_excel(writer, sheet_name="Resumo", index=False)
    resumo_df.to_excel(writer, sheet_name="Resumo", startrow=len(total_vendas) + 3, index=False)

print("✅ Relatório gerado com sucesso: relatorio.xlsx")
