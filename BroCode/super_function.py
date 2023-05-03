from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod

    def eat(self):
        pass

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        

class Elephant(Animal):
    
    def __init__(self, length, width, height):
        super().__init__(length,width,height)

    def eat(self):
        print("Esse elefante está comendo")

    def volume(self):
        return self.length*self.width
        
elephant = Elephant(10, 6, 10)

print("O volume desse elefante é: "+str(elephant.volume()))
