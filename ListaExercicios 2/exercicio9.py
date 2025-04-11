class Animal:
    def __init__(self):
        pass

    def fazer_som(self):
        print("Muuuuuu")

class Cachorro(Animal):
    def __init__(self):
        super().__init__()
    
    def fazer_som(self):
        print("Au Au")
class Gato(Animal):
    def __init__(self):
        super().__init__()
    def fazer_som(self):
        print("Miau")

obj1 = Animal()
obj1.fazer_som()

obj2 = Cachorro()
obj2.fazer_som()

obj3 = Gato()
obj3.fazer_som()