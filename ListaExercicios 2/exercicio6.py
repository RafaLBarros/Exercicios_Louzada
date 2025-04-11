try:
    x = int(input("Digite um numerador: "))
    y = int(input("Digite o denominador: "))
    print("A divisão dos dois números é:",x/y)
except ValueError:
    print("Deve digitar um número!")
except ZeroDivisionError:
    print("O denominador deve ser diferente de 0!")