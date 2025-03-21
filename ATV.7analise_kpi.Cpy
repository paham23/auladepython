import pandas as pd

# Função para calcular o Ticket Médio
def calcular_ticket_medio(df):
    # Calculando o valor total das vendas
    total_vendas = (df['Preco'] * df['Quantidade']).sum()
    # Calculando a quantidade total de produtos vendidos
    total_quantidade = df['Quantidade'].sum()
    # Calculando o Ticket Médio
    ticket_medio = total_vendas / total_quantidade
    return ticket_medio

# Função para identificar produtos com margem de lucro baixa (<20%)
def produtos_margem_baixa(df, limite_margem=20):
    # Definir preço de custo (vamos assumir que o preço de custo é 70% do preço de venda)
    df['Custo'] = df['Preco'] * 0.7
    # Calculando a margem de lucro
    df['Margem_Lucro'] = ((df['Preco'] - df['Custo']) / df['Preco']) * 100
    # Filtrando os produtos com margem de lucro inferior a 20%
    produtos_baixa_margem = df[df['Margem_Lucro'] < limite_margem]
    return produtos_baixa_margem[['Produto', 'Margem_Lucro']] if not produtos_baixa_margem.empty else None

# Função para identificar os Top 3 produtos mais lucrativos
def top_3_produtos_mais_lucrativos(df):
    # Calculando o lucro total de cada produto
    df['Lucro'] = (df['Preco'] - df['Custo']) * df['Quantidade']
    # Selecionando os top 3 produtos mais lucrativos
    top_3 = df.nlargest(3, 'Lucro')
    return top_3[['Produto', 'Lucro']] if not top_3.empty else None

# Dados fornecidos
dados = {
    'Produto': ['Shampoo Tucuma', 'Condicionador Cupuacu', 'Sabonete Acai', 'Oleo de Andiroba', 'Manteiga de Murumuru'],
    'Quantidade': [10, 5, 15, 8, 6],
    'Preco': [25.00, 30.00, 12.00, 40.00, 35.00]
}

# Carregar os dados em um DataFrame
df = pd.DataFrame(dados)

# Calcular o Ticket Médio
ticket_medio = calcular_ticket_medio(df)
print(f"Ticket Médio: R${ticket_medio:.2f}")

# Identificar produtos com margem de lucro baixa (limite de 20%)
produtos_baixa_margem = produtos_margem_baixa(df)
if produtos_baixa_margem is None:
    print("\nNenhum produto com margem de lucro baixa (<20%) encontrado.")
else:
    print("\nProdutos com margem de lucro baixa (<20%):")
    print(produtos_baixa_margem)

# Identificar os Top 3 produtos mais lucrativos
top_3_produtos = top_3_produtos_mais_lucrativos(df)
if top_3_produtos is None:
    print("\nNenhum produto lucrativo encontrado.")
else:
    print("\nTop 3 Produtos Mais Lucrativos:")
    print(top_3_produtos)
