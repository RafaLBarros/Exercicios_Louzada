times = ("Vasco","Fluminense","Botafogo","Madureira","Bragantino","Avai","Criciuma","Flamengo","Cruzeiro","Santos")
for i in range(3):
    print("Colocado",i+1,times[i])
for i in range(3):
    print("Colocado",10-i,times[9-i])
ordem = list(times)
ordem.sort()
for i in ordem:
    print("Times ordenados:",i)
x = int(input("Digite a colocação do time que quer procurar (1 a 10): "))
print(times[x-1])