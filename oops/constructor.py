class Hish:

    age = 22

    def __init__(self, name) -> None:
        self.name = name
        print('hello ssup')

    def __str__(self):
        return self.name
    
h1 = Hish('dul')
print(h1)

print(h1.age)
print(Hish.age)

