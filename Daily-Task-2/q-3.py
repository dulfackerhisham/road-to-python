class Rectangle():
    def __init__(self,height: int, width: int) -> None:
        self.height = height
        self.width = width

    def area(self):
        return f"area of rectangle is: {self.width * self.height}"
    
r1 = Rectangle(5, 10)

print(r1.area())