
class Base():
    _shared_dict = {}
    def __init__(self,num1):
        self.num1 = num1
        self.num3 = 10 

class A(Base):
    def __init__(self,num1,num2):
        self.num2 = num2
        super(A, self).__init__(num1 = num1)
        #self.num1 = 0 #output will change the baseclass value if changedandaccesed using oject




if __name__ == "__main__":
    obj1 = A(num1 =10,num2=20)
    print(f"__dict__ {obj1.__dict__}") # output: {'num2': 20, 'num1': 10, 'num3': 10} # note: num3 of base class also gets listed in Class A __dict__ 
    print(f"__dict__ {obj1.__class__.__dict__}") # output: {'__module__': '__main__', '__init__': <function A.__init__ at 0x7f5e3f23ed08>, '__doc__': None}
    print("\n\n",dir(obj1))

