x = list()
for i in range(4):
    frase = "Digite o " + str(i+1) + " número: "
    x.append(int(input(frase)))
tupla = tuple(x)
print("9 aparece",tupla.count(9),"vezes.")
print("3 aparece na posição",tupla.index(3))
for n in tupla:
    if n % 2 == 0:
        print(n,"é par")

