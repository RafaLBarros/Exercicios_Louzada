try:
    lista = [1,2,3,4,5]
    indice = int(input("Digite o indice para acessar da lista, de 0 a 4: "))
    print(lista[indice])
except ValueError:
    print("O valor deve ser um número inteiro!")
except IndexError:
    print("O valor deve ser entre 0 ou 4!")