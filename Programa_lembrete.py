import tkinter
import plyer

def lembrete(mensagem, atraso):
    try:
        time.sleep(atraso)
        plyer.notification.notify(
            title="Lembre ",
             messagem = mensagem, timeout=10
             )
    except Exception as e: 
        print(f"erro ao enviar notificação:{e}")
        mensagem = "Não esqueça de tomar água!"
        atraso=10
    lembrete(mensagem, atraso)
