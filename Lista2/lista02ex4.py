nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
if (nota1+nota2)/2 >= 7:
    print("Aprovado!")
elif (nota1+nota2)/2 >= 5:
    print("Em Recuperação!")
else:
    print("Reprovado!")