class Contador:
    def __init__(self,n):
        self.__n = n
        self.__i = 0

    def __iter__(self):
        return self

    def __next__(self):	
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        ret = self.__i
        return ret
    
for i in Contador(10):
    print(i)