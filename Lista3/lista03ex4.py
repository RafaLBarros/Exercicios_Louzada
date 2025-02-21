num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))
for i in range(num1,num2+1):
    if i%2 != 0:
        print(i,"é impar!")