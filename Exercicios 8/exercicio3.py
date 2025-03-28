def dobrar():
    try:
        num1 = int(input("Digite um valor inteiro: "))
        print("O Dobro desse valor é",num1*2)
    except(ValueError):
        print("O valor deve ser inteiro!")
        dobrar()
dobrar()