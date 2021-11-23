"""
Facade Design Pattern

In this Pattern we create a Class or Iterface which then Interacts with other classes
"""



class A:
    def __init__(self):
        print("Classs A Initialized")

    def get_details(self):
        return "Details of CLass A"


class B:
    def __init__(self):
        print("class B Initialized")

    def get_details(self):
        return "Detais of Class B"


class C:
    def __init__(self):
        print("CLass C Initialized")

    def get_details(self):
        return "Details of class C"

#This is the Interface which we will be interactin with for using other classes
class Facade:
    def __init__(self):
        self.obj_a = A()
        self.obj_b = B()
        self.obj_c = C()

    def get_all_details(self):
        result = {}
        result["a"] = self.obj_a.get_details()
        result["b"] = self.obj_b.get_details()
        result["c"] = self.obj_c.get_details()
        return result




if __name__ == "__main__":
    obj1 = Facade()
    result =obj1.get_all_details()
    print(result)