import pyautogui
import time

def menu()
    print("Olá amiga tudo bem:")
    print("1-Olá! espero que você esteja bem")
    print("2-Feliz aniversário")
    print("3-Obrigada Deus")
    print("4-Vamos ao shopping")

    def enviar_mensagem(mensagem):
        pyautogui.typewrite(mensagem)
        # digitar msg
        pyautogui.press('enter')
        #enviar a msg

        def main() 
        menu()
        escolha = input("2:")
        if escolha == '1'
        msg = "Olá! espero que você esteja bem"