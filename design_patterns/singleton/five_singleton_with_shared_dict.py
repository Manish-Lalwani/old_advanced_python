"""
Singleton Implementation with shared behaviour
ref link: https://www.youtube.com/watch?v=wElVjMlYVAw&list=PL1WVjBsN-_NK13Vf2UqdLZtukQ23TxeSx&index=7&ab_channel=AaravTech
Solution 2 but with same class
"""

#Regular Class
class A:
    def __init__(self,num1):
        self.num1 = num1
        print("__dict__ values are: ",self.__dict__)

#Singleton class with shared dict
class B:
    _shared_dict = {}

    def __init__(self,num1):
        print(f"__dict__ value at start of init is {self.__dict__} ")
        print("assigning shared dictionary to self.__dict__")
        self.__dict__ = self._shared_dict
        print(f"__dict__ value after assigning of init is {self.__dict__} ")
        self.num1 = num1


if __name__ == "__main__":
    obj1a = A(num1=5)
    print("First Object of Regular Class A created")
    print(f"__dict__ of obj1a: {obj1a.__dict__}")
    obj2a = A(num1=10)
    print("Second Object of Regular Class A created")
    print(f"__dict__ of obj2a: {obj2a.__dict__}")
    print(f"Address of Regular object is: obj1a {obj1a}  obj2a {obj2a}")
    print(f"Regular class objects __dict__ are obj1a:{obj1a.__dict__} obj2a:{obj2a.__dict__}")

    print("***********************************************************************************")

    obj1b = B(num1=5)
    print("First Object of Singleton Class B created")
    print(f"__dict__ of obj1b: {obj1b.__dict__}")
    obj2b = B(num1=10)
    print("Second Object of Regular Class A created")
    print(f"__dict__ of obj2a: {obj2b.__dict__}")
    print(f"Address of Singleton object is: obj1b {obj1b}  obj2b {obj2b}")
    print(f"Singleton class objects __dict__ are obj1b:{obj1b.__dict__} obj2b:{obj2b.__dict__}")
