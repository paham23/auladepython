arquivo = open('contatos.txt', 'r')
for linha in arquivo:
    print(linha)
arquivo.close()


arquivo = open('contatos.txt', 'a')
arquivo.write('\n jose')
arquivo.close()

