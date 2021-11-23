"""
Properties Decorator
Used to get, set and delete attribute
"""
#using regular class
class A:
    def __init__(self,name):
        self.__name = name


    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def del_name(self):
        del self.__name

#using properties
class B:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        print("Getter called")
        return self.__name

    @name.setter
    def name(self,name):
        print("Setter called")
        self.__name = name

    @name.deleter
    def name(self):
        print("Deleter called")
        del self.__name

#using property constructor and passing the method as argumment
class C:
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        print("Getter called")
        return self.__name

    def set_name(self,name):
        print("Setter called")
        self.__name = name

    def del_name(self):
        print("Deleter called")
        del self.__name

    name = property(fget=get_name,fset=set_name,fdel=del_name,doc="this is doc string") #property class constructor

if __name__ == "__main__":
    obj1 = A(name="Shubham")
    print("printing private variable",obj1._A__name) #we can directly print private variable by prefixing _classname_ to the variable
    print("__dict__",obj1.__dict__)
    print(obj1.get_name())
    obj1.set_name(name ="Aditya")
    print("after changing:",obj1.get_name())
    obj1.del_name()
    print("after deleting object __dict__: ", obj1.__dict__)

    print("###################\n")
    obj2 = B(name="Rahul")
    print("__dict__", obj2.__dict__)
    print(obj2.name)
    obj2.name = 24
    print("after changing:", obj2.name)
    del obj2.name
    print("after deleting object __dict__: ", obj2.__dict__)

    print("###################\n")
    obj3 = C(name="SUjay")
    print("__dict__", obj3.__dict__)
    print(obj3.name)
    obj3.name = 48
    print("after changing:", obj3.name)
    del obj3.name
    print("after deleting object __dict__: ", obj3.__dict__)




    