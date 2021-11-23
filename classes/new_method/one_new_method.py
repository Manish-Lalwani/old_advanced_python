import my_beautify as mb
import inspect
"""
ref link : https://dev.to/pila/constructors-in-python-init-vs-new-2f9j#:~:text=__new__%20is%20the,instance%20after%20it's%20been%20created.
ref link : https://dev.to/delta456/python-init-is-not-a-constructor-12on
Unlike other programming languages for creating object in python there is a 2 step process

__new__ and __init__

__new__ function is called 
"""
details_flag = 0
class A:
    """Normal calling"""
    stack = inspect.stack()
    mb.details(stack, details_flag)
    def __init__(self,num1,num2): #here new method was called internally which created the instance of the class and passed it to __init__ which was stored in self parameter
        stack = inspect.stack()
        mb.details(stack, details_flag)
        self.num1 = num1
        self.num2 = num2


class B:
    """using __new__ keyword"""
    stack = inspect.stack()
    mb.details(stack, details_flag)
    def __new__(cls,num1,num2):  #here we are calling mew method explicitly here cls points to class the new method creates the instance of the class which is pointed by cls and returns it's instance
        print("New method--------")
        stack = inspect.stack()
        mb.details(stack, details_flag)
        print(cls,"----",type(cls))
        new_obj = object.__new__(cls)
        print(new_obj,"----",type(new_obj))
        return new_obj

    def __init__(self,num1,num2): # after we got the instance from new in self parameter now we can use self for initializing methods and properties.
        print("\nInit method--------")
        stack = inspect.stack()
        mb.details(stack, details_flag)
        self.num1 = num1
        self.num2 = num2

if __name__ == "__main__":  # This is <module> function as the code is executing from module and if __name__ is just an if condition
    stack = inspect.stack() #function='<module>'
    #mb.details(stack, details_flag) #caller_func = stack[1][0].f_code.co_name IndexError: list index out of range
    #print(stack)

    a = A(num1=5,num2=6)
    print(f"heap location of object a after init is {a}")  # will print the heap location
    print(f"class A values are num1={a.num1} num2={a.num2}\n")

    b = B(num1=5,num2=6)
    print(f"heap location of object a after init is {b}")  # will print the heap location
    print(f"class A values are num1={b.num1} num2={b.num2}\n")

    print(repr(int.__mro__))






