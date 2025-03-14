x = []
while(True):
    num = int(input("Digite um valor para colocar na lista! (-1 para parar): "))
    if(num == -1):
        break
    x.append(num)
print(x)
val = int(input("Digite o numero que quer contar! "))
print(val,"aparece",x.count(val),"vezes!")