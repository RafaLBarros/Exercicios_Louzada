try:
    num1 = float(input("Digite o primeiro valor numerico: "))
    num2 = float(input("Digite o segundo valor numerico: "))
    print("A divisão dos dois números é",num1/num2)
except(ZeroDivisionError):
    print("O valor de divisão não pode ser 0!")
except(ValueError):
    print("O valor deve ser numerico!")



