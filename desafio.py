def menu():
    #é responsavel por exibir as opções disponiveis para o usuario. Ela apresenta uma lista de escolhas que o usuario pode fazer.
    print("1-padrão\n2-Personalizada\n3-Agradecimento\n4-sair")

def main():
    #é ponto de entrada principal do programa. ela controla o fluxo de exercução e contém a logica 
    while True:

    #laço de repetição recebe, são estruturas de controle em programação que permitem executar um 
    #bloco de código várias vezes, enquanto uma condição especifica for verdadeira. 
    #eles são usados para automatizar tarefas repetitivas
        menu()
        #chama a função menu para mostrar as opções 
        escolha=input("Escolha:")
        if escolha == '1':
        #que permite executar um bloco de código somente se uma condição especifica for verdadeira.
            print("Olá! esta é uma msg padrão.")
        elif escolha == '2':
            print(input("Msg personalizada:"))
        elif escolha == '3':
            print("Obrigada por tudo!")
        elif escolha == '4':
            #é uma abreviação de "else if" e é usado em estruturascondicionais para verificar múltiplas condições 
            #ele permite que vc teste uma nova condição anterior no if for falsa
            break
        #encerra o código
        
        else: 
            #Else captura todas as entradas que não correpondem às opções válidas(1, 2, 3 ou 4) quando o usuario digita uma opção
            #inválida, o programa informa que a opção é invalida e pede que ele tente novamente, permitindo assim que o usuario continue 
            #interagindo com o menu 
            print("opção invalida.")
if __name__=="__main__":
 main()