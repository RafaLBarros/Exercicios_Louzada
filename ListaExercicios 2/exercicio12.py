def multiplicador(fator):
    local = fator
    def func(n):
        return n*fator
    return func

mult = multiplicador(3)
for i in range(10):
    print(mult(i))