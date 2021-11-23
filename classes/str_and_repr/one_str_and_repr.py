"""
str and repr method

ref ink: https://www.journaldev.com/22460/python-str-repr-functions

Well, the __str__ function is supposed to return a human-readable format, which is good for logging or to display some information about the object. Whereas, the __repr__ function is supposed to return an “official” string representation of the object, which can be used to construct the object again
"""


class A:
    def __init__(self):
        print("This is init method")


class B:
    def __init__(self):
        print("This is init method")


    def __str__(self):
       return "printing from str method"

    # def __repr__(self):
    #     return "printing from repr"

class C:
    def __init__(self):
        print("This is init method")


    def __str__(self):
       return "printing from str method"

    def __repr__(self):
        return "printing from repr"


class D:
    def __init__(self,num1):
        print("This is init method")

    def __str__(self):
       return "printing from str method"

    def __repr__(self):
        return "C(num1=5)"


if __name__ == "__main__":
    obj = A()
    print(obj) #output: <__main__.A object at 0x7f58aa953dd8>
    print(obj.__str__()) #output: <__main__.A object at 0x7f58aa953dd8>
    print(obj.__repr__()) #output: <__main__.A object at 0x7f58aa953dd8>

    """
    output:
    This is init method
    <__main__.A object at 0x7f58aa953dd8>
    <__main__.A object at 0x7f58aa953dd8>
    <__main__.A object at 0x7f58aa953dd8>

    """
    print("\nPrinting from class B")
    obj1 = B()
    print(obj1) #output: printing from str method
    print(obj1.__str__()) #output: printing from str method
    print(obj1.__repr__())#output: <__main__.B object at 0x7effb710be80>


    """
    This is init method
    printing from str method
    printing from str method
    <__main__.B object at 0x7effb710be80>
    """


    print("\nPrinting from class C")
    obj2 = C()
    print(obj2) #output: printing from str method
    print(obj2.__str__()) #output: printing from str method
    print(obj2.__repr__())#output: printing from repr


    """
    Printing from class C
    This is init method
    printing from str method
    printing from str method
    printing from repr
    """