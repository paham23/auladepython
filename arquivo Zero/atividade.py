file = open("texto.txt", "r")
for linha in file: 
    print(linha)

file.close()
arquivo = open('texto.txt', 'r')
def contar(palavra):
    vogais = 'aeiou'
    conta = 0 
    for vogal in palavra:
        if vogal in vogais:
            conte+=1 
    return conta 
palavra = str(input("Digite a palava: " ))
print(contar(palavra))
for linha in arquivo:
    print(linha)
    arquivo.close()
