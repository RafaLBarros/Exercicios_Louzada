x = input("Digite varias palavras separadas por espaço: ")
y = x.split()
y.sort()
print("Ordenado:",y)
print("Quantidade de palavras:",len(y))
maiusculo = []
for palavra in y:
    maiusculo.append(palavra.upper())
print("Maiúsculo:",maiusculo)