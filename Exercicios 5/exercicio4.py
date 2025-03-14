def vogais(palavra):
    soma = 0
    for char in palavra:
        if char in ['a','e','i','o','u','A','E','I','O','U','á','Á','à','À','é','É','í','Í','ó','Ó','ú','Ú','â','Â','ô','Ô','ã','Ã','õ','Õ']:
            soma += 1
    return  soma

palavra = input("Digite uma palavra: ")
print("Essa palavra possui",vogais(palavra),"vogais!")
