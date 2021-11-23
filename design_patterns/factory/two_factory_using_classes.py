"""
Factory Design pattern with Class
ref link : https://stackabuse.com/the-factory-method-design-pattern-in-python/
"""

"""
Base Class needs to either Inherit Class ABC or use metaclass=ABCMeta and secondly it needs to use decorator abstractmethod for all functions 
Class Inheriting Abstract Class has to implement all methods  or else typeError is thrown
"""
from abc import ABCMeta,abstractmethod,ABC

class Shape(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Square(Shape):
    def __init__(self):
        print("Square Initialize")
    # IF NOT ALL METHOD OF sHAPE CLASS ARE OVERRIDED IT THROWS AN ERROR : TypeError: Can't instantiate abstract class Square with abstract methods calculate_area, calculate_perimeter
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self,breadth,width):
        self.breadth = breadth
        self.width = width
        super(Rectangle, self).__init__()

    def calculate_area(self):
        return 2*(self.breadth + self.width)

    def calculate_perimeter(self):
        pass


class ShapeFactory:
    def __init__(self):
        print("INITIALIZING FACTORY METHOD")

    def create_shape(self,name): #factory method
        if name.lower() =="square":
            size = input("Enter the size of square")
            return Square()
        elif name.lower() == "rectangle":
            height = input("Enter height of rectactory ngle")
            width = input("Enter width of rectangle")
            return Rectangle(height,width)



if __name__ == "__main__":
    #Without Factory Method
    # obj_square = Square()
    # obj_rectangle = Rectangle(breadth=10,width=20)

    #Using Factory
    #obj_square = ShapeFactory("square")
    obj_shape_factory = ShapeFactory()
    obj_rectangle = obj_shape_factory.create_shape("square")
    print(type(obj_rectangle))
    obj_rectangle.calculate_area()


