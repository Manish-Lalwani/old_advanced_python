"""
SLots with Inheritance

Note: There can be issue using __slots__ in multiple inheritance if both class A and B use slots in this case the child class will get error while defining __slots__
solution for this problem is that one class should have empty slot
"""

class A:
    __slots__ = ["name","__dict__"]
    def __init__(self):
        self.name = name

class B:
    __slots__ = ["num"]
    def __init__(self):
        self.num = num


class C(A,B):
    __slots__ = ["roll_no"]
    def __init__(self,name,num,roll_no):
        self.num = num
        self.name = name
        self.roll_no = roll_no


if __name__ == "__main__":
    obj1 = C()



