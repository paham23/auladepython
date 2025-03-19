#crie um programa de lembrente de tomar agua a biblioteca plyer
from plyer import notification     #importando a biblioteca plyer para criar uma notificação.

# Função para exibir a notificação 
def lembrete(titulo, mensagem):
    notification.notify(
        title=titulo,
        message=mensagem,
        app_name='Lembrete',
        timeout=5  # duração de notificação em segundos 
    )
    #Exibindo o lembrete.
lembrete("Bora beber água, o rim pedi socorro!!", "Tu tem que tomar agua pra evitar pedras")