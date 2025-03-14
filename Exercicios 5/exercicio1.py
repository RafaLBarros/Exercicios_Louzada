def fat(x):
    val = x
    while(x-1 != 0):
        val = val*(x-1)
        x -= 1
    return val

val = int(input("Digite um valor numerico para checar sua fatorial! "))
x = fat(val)
print(x)