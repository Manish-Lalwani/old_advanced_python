class A:
    def __init__(self,name,surname):
        #protected variables
        self._name = name
        self._surname = surname


class B(A):
    def __init__(self,iname,isurname):
        super().__init__(name=iname,surname=isurname)

    def base_class_var_print(self):
        print(f"Accessing protected variable of Base class A self._name {self._name}, self._surname {self._surname}")


if __name__ == "__main__":
    obj = A(name="Suresh",surname="Agarwal")
    print(f"First  is:{obj._name},Last  is:{obj._surname} ") #protected variables in python are still accessible
    obj2 = B(iname="Bitto",isurname="Sharma")
    obj2.base_class_var_print() #the correct way to access protected variable(through derived class function in python
