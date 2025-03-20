import pandas as pd
import smtplib
import os
from email.message import EmailMessage

# Configurações do e-mail
EMAIL_REMETENTE = "seuemail@gmail.com"
EMAIL_SENHA = "sua_senha_de_app"  # Para Gmail, use uma senha de app
EMAIL_DESTINATARIO = "destinatario@email.com"

# 1. Ler o arquivo CSV
df = pd.read_csv("vendas.csv")

# 2. Calcular total vendido por produto
df["Total"] = df["Quantidade"] * df["Preço"]
total_vendas = df.groupby("Produto", as_index=False)["Total"].sum()

# 3. Identificar o produto mais vendido
produto_mais_vendido = total_vendas.loc[total_vendas["Total"].idxmax()]

# 4. Criar o relatório em Excel
arquivo_excel = "relatorio.xlsx"
with pd.ExcelWriter(arquivo_excel, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Vendas", index=False)
    total_vendas.to_excel(writer, sheet_name="Resumo", index=False)
    
    resumo_df = pd.DataFrame({
        "Produto mais vendido": [produto_mais_vendido["Produto"]],
        "Total vendido (R$)": [produto_mais_vendido["Total"]],
        "Total geral de vendas (R$)": [total_vendas["Total"].sum()]
    })
    resumo_df.to_excel(writer, sheet_name="Resumo", startrow=len(total_vendas) + 3, index=False)

print("Relatório gerado com sucesso!")

# 5. Criar o e-mail
msg = EmailMessage()
msg["Subject"] = "Relatório de Vendas"
msg["From"] = EMAIL_REMETENTE
msg["To"] = EMAIL_DESTINATARIO
msg.set_content(
    f"Olá,\n\nSegue em anexo o relatório de vendas.\n\n"
    f"Produto mais vendido: {produto_mais_vendido['Produto']} (R$ {produto_mais_vendido['Total']:.2f})\n"
    f"Total geral de vendas: R$ {total_vendas['Total'].sum():.2f}\n\n"
    "Atenciosamente,\nSistema de Relatórios"
)

# 6. Anexar o relatório
with open(arquivo_excel, "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="xlsx", filename=arquivo_excel)

# 7. Enviar o e-mail
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_REMETENTE, EMAIL_SENHA)
        server.send_message(msg)
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f" Erro ao enviar e-mail: {e}")
