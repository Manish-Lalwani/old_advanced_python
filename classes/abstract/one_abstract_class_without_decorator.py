"""
Abstract Class and it's functionalities
"""
from abc import ABC,abstractmethod



class Shapes(ABC):
    #@abstractmethod
    def __init__(self):
        self.height = None #we can declare variables in abstract method
        self.width = None

    #@abstractmethod
    def area(self):
        pass
    #@abstractmethod
    def get_height(self):
        pass

    #@abstractmethod
    def get_width(self):
        pass





class Rectangle(Shapes):
    def __init__(self,height,width):
        self.height = int(height)
        self.width = int(width)
        #super().__init__()
        print("printing local argument",height)
        print("inside init", self.height)
        #super(Shapes,self).__init__(self)

    def area(self):
        print("inside area",self.height)
        return self.height * self.width


    def get_height(self):
        pass

    def get_width(self):
        pass



if __name__ == "__main__":
    r1 = Rectangle(height=5,width=10)
    r1.area()