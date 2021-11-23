"""
Creating singleton objet with the help of class
"""
import inspect

class MetaClass(type):
    instance = None
    def __new__(cls,class_name,base,attr):
        print("\n#InsideMetaClass New Method")
        #print(f"cls {cls}, class_name {class_name}, base {base}, attr {attr}")
        if cls.instance == None:
            temp_instance = super(MetaClass,cls).__new__(cls,class_name,base,attr)
            cls.instance = temp_instance
        return temp_instance

    def __init__(self,class_name,base,attr): #executing
        print("#MetaClass Init Method")
        print("printinh : ",self.__dict__)
        super(MetaClass,self).__init__(class_name,base,attr) #in super init no need to provide cls or self argument

    # def __init__(cls):
    #     print("#MetaClass Init Method")


class A(metaclass=MetaClass):
    x = 10
    y =10

    def __init__(self):
        print("#A Init Method")
        super(A,self).__init__()
    #     super(A,self).__init__(self,class_name,base,attr)

    # def __init__(self):
    #     super(A,self).__init__(self)
    #     print("#A Init Method")


    # def __call__(self):
    #     print("#A Call Method")

    def func1(self):
        print("#A func1 Method")


if __name__ == "__main__":
    obj1 = A()
    print(f"base class of A is {inspect.getmro(A)}")
    print(f"-obj is allocated @{obj1}, --obj.x is {obj1.x}, --obj.y is {obj1.y}\n\n")
    print("Creating second object")
    obj2 = A()
    print(f"-obj is allocated @{obj2}, --obj.x is {obj2.x}, --obj.y is {obj2.y}\n\n")


