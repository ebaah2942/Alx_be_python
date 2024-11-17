
import math


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise Exception("NotImplementedError: derived classes need to override this method.")
    
        



    def __str__(self):
        return f"{self.name} with area {self.area()} and perimeter {self.perimeter()}"
    

class Rectangle(Shape):
    def __init__(self, length, width, name="Rectangle"):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
        



class Circle(Shape):
    def __init__(self, radius, name="Circle"):   
        super().__init__(name)
        self.radius = radius 

    def area(self):
        return math.pi * self.radius** 2
       




def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()          

    