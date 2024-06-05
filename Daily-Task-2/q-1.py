class Person():
    def __init__(self,name, age) -> None:
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hey {self.name}, how you doing")

p1 = Person("hisham", 22)

p1.greet()