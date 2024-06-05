class Person:
    def __init__(self, name, occu, netw) -> None:
        self.name = name
        self.occu = occu
        self.netw = netw

    def show(self):
        print(f"{self.name} is working as {self.occu} and have networth of {self.netw}")

  
a = Person()

a.show()