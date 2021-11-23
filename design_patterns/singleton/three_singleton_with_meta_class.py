"""
Singleton with Meta class
"""


class Meta(type):
    def __new__(cls, class_name,base,attr):
        instance = super(Meta,cls).__new__(cls,class_name,base,attr) #calling type constructor as we have inherited type super is same as type
        print("inside Meta",instance)
        return instance




class A(metaclass=Meta):
    def __new__(cls,class_name,base,attr): #experiment if metaclass is specified the new method of this class will not execute
        print("inside A", instance)
        instance = super(A, cls).__new__(cls, class_name, base,attr)  # calling type constructor as we have inherited type super is same as type
        print("inside A", instance)

    def __init__(self): #init method will also not be excuted
        print("inside A __init__")

    def __call__(self, *args, **kwargs): #call method will also not be executeddd
        print("inside A __call__")