import pandas as pd
from plyer import notification

# 1. Lendo o arquivo CSV
df = pd.read_csv("vendas.csv")

# 2. Calculando o total vendido por produto
df["Total"] = df["Quantidade"] * df["Preço"]
total_vendas = df.groupby("Produto")["Total"].sum()

# 3. Identificando o produto mais vendido
produto_mais_vendido = total_vendas.idxmax()
valor_mais_vendido = total_vendas.max()

# 4. Calculando o total geral das vendas
total_geral_vendas = total_vendas.sum()

# 5. Criando a notificação
mensagem = (
    f"Produto mais vendido: {produto_mais_vendido} (R$ {valor_mais_vendido:.2f})\n"
    f"Total geral de vendas: R$ {total_geral_vendas:.2f}"
)

# 6. Enviando a notificação
notification.notify(
    title="Resumo das Vendas",
    message=mensagem,
    app_name="Sistema de Vendas",
    timeout=10  # Tempo que a notificação ficará visível
)

print("Notificação enviada com sucesso!")
