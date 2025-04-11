class Livro:
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def __str__(self):
        return "Titulo: " + self.titulo + "\nAutor: " +self.autor + "\nPáginas: " + str(self.paginas)
    def __len__(self):
        return self.paginas

obj1 = Livro("Crepúsculo","Stephenie Meyer",420)
obj2 = Livro("O Senhor dos Anéis: A Sociedade do Anel","J. R. R. Tolkien",576)

print(obj1.__str__())
print(obj1.__len__())
print(obj2.__str__())
print(obj2.__len__())