"""
REGARDING __CALL__ METHOD
ref link: https://stackoverflow.com/questions/9663562/what-is-the-difference-between-init-and-call
"""

class A:
    """Normal Class"""
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2


class B:
    """Class with Callable"""
    #def __call__(self, *args, **kwargs):
    def __call__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2



class C:
    """Class using both"""
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def __call__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2




if __name__ == "__main__":
    a = A(num1=5,num2=6)
    print(f"heap location of object a after init is {a}")  # will print the heap location
    print(f"class A values are num1={a.num1} num2={a.num2}")
#    a(num1=10,num2=11) #getting error TypeError: 'A' object is not callable #we get this error because we are calling object of class a as a function
    a = A(num1=10, num2=11)
    print(f"heap location of object a after init is {a}")  # will print the heap location
    print(f"class A values are num1={a.num1} num2={a.num2}\n")


    """
    so for calling an object as a function we use __call__ method other benefit of this methos is that we can change the values afterwards
    we will see this in CLass B example
    """
    #b = B(num1=5,num2=6) #TypeError: object() takes no parameters # as we are using __call__ instead of __init__ , so the instantiation will be
    b = B()
    b(num1=5, num2=6)
    print(f"heap location of object b after init is {b}")  # will print the heap location
    print(f"class B values are num1={b.num1} num2={b.num2}")
    b(num1=10, num2=11)
    print(f"heap location of object b after init is {b}") #will print the heap location #object remains the same unlike a where new object was created
    print(f"class B values are num1={b.num1} num2={b.num2}\n")



    c = C(num1=5,num2=6)
    print(f"heap location of object c after init is {c}")  # will print the heap location
    print(f"class C values are num1={c.num1} num2={c.num2}")
    c(num1=10, num2=11)
    print(f"heap location of object c after init is {c}")  # will print the heap location
    print(f"class C values are num1={c.num1} num2={c.num2}")







