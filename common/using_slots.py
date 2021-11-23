"""
Using slots we can restrict addition of new variable at runtime
ALso SLot variables access time and memory consumtion is lesser
"""
class A:
    __slots__ = ["name","age"]
    def __init__(self,name,age):
        self.name = name
        self.age = age

        #self.get_info()

    def get_info(self):
        print("Name is:",self.name)
        print("Age is:",self.age)



if __name__ == "__main__":
    obj1 = A(name="Shubham",age=39)
    obj1.roll_no = 1 #trying to add new attribute will give error


