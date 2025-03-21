produtos = {1:("Arroz",10.00),
            2:("Feijão",8.00),
            3:("Chiclete",3.50),
            4:("Picanha",70.00),
            5:("Lápis",3.90)}
codigo = int(input("Digite o código do produto: "))
if (codigo in produtos.keys()):
    print(f"Produto {codigo} -> Nome: {produtos[codigo][0]}, Valor: {produtos[codigo][1]}")
else:
    print("Código de produto não existente.")