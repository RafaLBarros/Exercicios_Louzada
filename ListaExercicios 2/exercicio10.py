def par(n):
    for i in range(n):
        yield i*2

x = int(input("Digite quantos pares quer gerar: "))
for v in par(x):
    print(v)