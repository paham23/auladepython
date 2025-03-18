import time 
#importação da biblioteca time, biblioteca time serve para manipular data e hora 

import random 
#é uma função que serve para realizar operações de forma aleatoria os elementos de alguma lista.

listaContatos = []
#declaração de uma lista vazia

while True:
    #laço de repetição recebe, são estrturas de controle em programação que permitem executar um 
    #bloco de código várias vezes, enquanto uma condição especifica for verdadeira. 
    #eles são usados para automatizar tarefas repetitivas

    listaContatos.append(input("Digite os nomes"))
    #verificando se o usuario deseja adicionar mais nomes 
    maisnomes = input("deseja continuar: ").lower()
    #caso digite n o laço de repetição para


    if maisnomes == "n" :
        break 
    #criando a função para mostrar msg na tela
def msg(lista):
    # mostrando msg na tela e usando o random para sortear o nome

    print(f"Boa Noite {random.choice(lista)}")
    #com o time  a msg será exebida de 2 em 2 minutos 

    time.sleep(2)
    print("Python")
    #chamando a função para amostar msg na tela com a listaContatos como paramentro
msg(listaContatos)