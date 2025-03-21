from email import encoders
import smtplib
import pandas as pd
from email.message import EmailMessage
from email.message import EmailMessage
from email.message import EmailMessage
from email.message import EmailMessage
from email.message import EmailMessage
from datetime import datetime

df = pd.read_csv("vendas.csv")
df["Total"] = df["Quantidade"] * df["Preço"]
resumo_vendas = df.groupby("Produto").agg({"Quantidade": "sum", "Total": "sum"}).reset_index()
resumo_vendas.to_excel("relatorio.xlsx", index=False)

EMAIL_REMETENTE = "seuemail@gmail.com"
EMAIL_SENHA = "sua_senha_de_app"  
EMAIL_DESTINATARIO = "destinatario@email.com"


msg = EmailMessage()
msg["From"] = EMAIL_REMETENTE
msg["To"] = EMAIL_DESTINATARIO
msg["Subject"] = "Relatório de Vendas"

corpo_email = """
Olá,

Segue em anexo o relatório de vendas automaticamente. 

anteciosamente, 
Automação de vendas 

"""
msg.attach(EmailMessage(corpo_email, "plain"))


anexo = open("relatorio.xlsx", "rb")
parte = EmailMessage("application", "octet-stream")
parte.set_payload(anexo.read())
encoders.encode_base64(parte)
parte.add_header("Content-Disposition", f"attachment; filename=relatorio.xlsx")
msg.attach(parte)
anexo.close()

servidor = smtplib.SMTP("smtp.gmail.com", 587)
servidor.starttls()
servidor.login("email_remetente, email_senha")
servidor.sendmail("email_remetente, email_destinatario, msg.as_string"())

print("\n email enviado com sucesso!")

