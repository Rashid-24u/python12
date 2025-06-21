from abc import ABC, abstractmethod
class Animal(ABC):   # Abstract class
    @abstractmethod
    def make_sound(self):
        pass # Abstract method
class Dog(Animal): # Concrete class
    def make_sound(self):
        return "Woof!"
class Cat(Animal): # Concrete class
    def make_sound(self):
        return "Meow!"
# Client code
dog=Dog()
cat=Cat()
print(dog.make_sound()) # Output: Woof!
print(cat.make_sound()) # Output: Meow !