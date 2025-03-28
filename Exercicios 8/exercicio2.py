try:
    nome = input("Me fale o nome do arquivo para leitura, com seu tipo: ")
    arquivo = open(nome,'r')
    conteudo = arquivo.read()
    print(conteudo)
except IOError:
    print("Arquivo não encontrado")
    