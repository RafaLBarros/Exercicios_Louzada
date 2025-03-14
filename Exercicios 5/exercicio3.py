def media(lista):
    soma = 0
    for val in lista:
        soma += val
    return soma/len(lista)

x = []
while(True):
    num = int(input("Digite um valor para colocar na lista! (-1 para parar): "))
    if(num == -1):
        break
    x.append(num)
print("A media dessa lista é",media(x))