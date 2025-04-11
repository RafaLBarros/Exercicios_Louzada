class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def exibirDetalhes(self):
        print("Marca:",self.marca)
        print("Modelo:",self.modelo)
        print("Ano:",self.ano)


obj = Carro("Volkswagen","Fusca","1959")
obj.exibirDetalhes()
obj2 = Carro("Honda","Civic","2022")
obj2.exibirDetalhes()