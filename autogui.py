import pyautogui

def msg():
    print('1 - Bom dia!')
    print('2 - Boa tarde!')
    print('3 - Boa noite!')
    op = 0 
    op = int(input('Digite a opção de Mensagem!'))
    match op:
        case 1:
            return "Bom dia!"
        case 2: "Boa Tarde"
            return "Boa Tarde"
        case 3:
            return "Boa Noite"

def menu ():
    print('Mensagens WhatsApp')
    print('1 - Mensagens Prontas')
    print('2 - Digitar sua mensagens')
    op = int(input('Escolha sua opção:'))
    return op
op = menu()
if op == 1: 