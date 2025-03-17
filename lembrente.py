import time
def lembrete_atividade(intervalo_minutos=10):
    contador = 1
    while True:
        print(f"\n Tempo encerrado(Lembrete{contador})")
        contador += 1
        time.sleep(intervalo_minutos*60)
lembrete_atividade()
