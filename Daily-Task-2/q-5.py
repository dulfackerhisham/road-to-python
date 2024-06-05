class Car():
    def __init__(self,make: str, model: int) -> None:
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} have started")

class ElectricCar(Car):
    def start(self):
        print(f"{self.make} have no sound")

c1 = Car("toyota", 2022)
c1.start()

e1 = ElectricCar("Tesla", 2023)
e1.start()