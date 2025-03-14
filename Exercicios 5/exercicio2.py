def primo(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
                break
        else:
            return True
    else:
        return False


val = int(input("Digite um valor numerico para checar se é primo! "))
x = primo(val)
if(x):
    print("É primo!")
else:
    print("Não é primo!")

