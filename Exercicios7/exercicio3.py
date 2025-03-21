dicionario = {"carro":"car",
              "chave":"key",
              "jogo":"game",
              "gato":"cat",
              "cachorro":"dog"}
palavra = input("Digite uma palavra em português: ")
if (palavra in dicionario.keys()):
    print("A tradução de",palavra,"é:",dicionario[palavra])
else:
    print("Palavra não armazenada no dicionário.")
