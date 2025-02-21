num = int(input("Digite o número de termos n de Fibonnacci: "))
termo2 = 1
aux = 0
termo = 0
for i in range(1,num+1):
    print(str(i)+"º","termo é ",termo)
    aux = termo2
    termo2 += termo
    termo = aux