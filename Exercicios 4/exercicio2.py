x = []
maior = -999999
menor = 99999999999
while(True):
    num = int(input("Digite um valor para colocar na lista! (-1 para parar): "))
    if(num == -1):
        break
    x.append(num)
    if(num > maior):
        maior = num
    if(num < menor):
        menor = num
print(x)
print("O maior é",maior)
print("O menor é",menor)