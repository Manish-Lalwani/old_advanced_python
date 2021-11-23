"""
Singleton Implementation with Shared Dictionary and Inheritance
ref link: https://www.youtube.com/watch?v=wElVjMlYVAw&list=PL1WVjBsN-_NK13Vf2UqdLZtukQ23TxeSx&index=7&ab_channel=AaravTech
Solution 2 but with Inheritance
"""


class Singleton():
    _shared_dict = {}
    def __init__(self,num1):
        self.__dict__ = self._shared_dict
        self.num1 = num1
        self.num3 = 10

class A(Singleton):
    def __init__(self,num1,num2):
        self.num2 = num2
        super(A, self).__init__(num1=num1)




if __name__ == "__main__":
    obj1 = A(num1=5,num2=10)
    print("First Object of Class A created")
    print(f"__dict__ of obj1: {obj1.__dict__}")
    obj2 = A(num1=20,num2=40)
    print("Second Object of Class A created")
    print(f"__dict__ of obj2: {obj2.__dict__}")
    print(f"Address of Singleton object is: obj1b {obj1}  obj2b {obj2}")
    print(f"Singleton class objects __dict__ are obj1b:{obj1.__dict__} obj2b:{obj2.__dict__}")



