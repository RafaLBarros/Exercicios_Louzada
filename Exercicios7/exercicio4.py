palavras = {}
frase = input("Digite uma frase: ")
x = frase.split(" ")

for palavra in x:
    palavras[palavra] = x.count(palavra)
for chave, valor in palavras.items():
    print(f"{chave}: {valor}")