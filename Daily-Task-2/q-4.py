class Animal():
    def __init__(self,name: str, species: str) -> None:
        self.name = name
        self.species = species

    def make_sound(self):
        print(f" {self.name} is making no sounds")

a1 = Animal("jimms", "italian")
a1.make_sound()

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} is making Meow sound")

c1 = Cat("tommy", "persian")
c1.make_sound()

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} is barkking gharrr")

d1 = Dog("rocky", "stallion")
d1.make_sound()