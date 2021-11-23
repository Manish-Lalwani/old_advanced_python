"""
Singleton Pattern
"""


class A:
    instance_list = [] #class variable list
    def __new__(cls):
        if len(cls.instance_list) ==0: #instance is not created
            instance = super(A,cls).__new__(cls)
            cls.instance_list.append(instance)
            return cls.instance_list[0]
        else:                     #instance is already created will return the already created instance
            print("Else executed")
            return cls.instance_list[0]



obj = A()
obj1 = A()

print(obj)
print(obj1)


