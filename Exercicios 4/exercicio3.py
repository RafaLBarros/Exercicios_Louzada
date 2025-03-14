x = []
while(True):
    num = int(input("Digite um valor para colocar na lista! (-1 para parar): "))
    if(num == -1):
        break
    x.append(num)
print(x)
x = set(x)
print(x)