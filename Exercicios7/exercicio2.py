letras = {}
palavra = input("Digite uma palavra: ")

for char in palavra:
    letras[char] = palavra.count(char)
for chave, valor in letras.items():
    print(f"{chave}: {valor}")