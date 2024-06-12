from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def types(self):
        pass

class lion(animal):
    def types(self):
        return "mammal"

class snakes(animal):
    def types(self):
        return "Reptiles"

class crow(animal):
    def types(self):
        return "Birds"
    
obj = crow()
print(obj.types())

obj = snakes()
print(obj.types())

obj = lion()
print(obj.types())

# obj = animal() # TypeError: Can't instantiate abstract class animal without an implementation for abstract method 'types'
# print(obj)