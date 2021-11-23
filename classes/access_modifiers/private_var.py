class A:
    def __init__(self,name,surname):
        #protected variables
        self.__name = name
        self.__surname = surname


class B(A):
    def __init__(self,iname,isurname):
        super().__init__(name=iname,surname=isurname)

    def base_class_var_print(self):
        print(f"Accessing protected variable of Base class A self._name {self.__name}, self._surname {self.__surname}")

if __name__ == "__main__":
    obj = A(name="Suresh",surname="Agarwal")
    #print(f"First  is:{obj.__name},Last  is:{obj.__surname} ") #AttributeError: 'A' object has no attribute '__name'
    obj2 = B(iname="Bitto",isurname="Sharma")
    #obj2.base_class_var_print() #AttributeError: 'B' object has no attribute '_B__name'


#Python performs name mangling of private variables. Every member with double underscore will be changed to _object._class__variable. If so required, it can still be accessed from outside the class, but the practice should be refrained.
    print(obj._A__name) #accessible
