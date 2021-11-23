"""
Creating MEtaClass
ref link: https://www.youtube.com/watch?v=NAQEj-c2CI8&ab_channel=TechWithTim
"""

class Meta(type): #this is the meta class which inherits type
    def __new__(cls,class_name,base,dict):
        return super(Meta,cls).__new__(cls,class_name,base,dict) #calling type __new__


class A(metaclass=Meta):
    x =5
    y =6

    def f1(self):
        print("inside f1")


obj = A()
print(obj)#output: <__main__.A object at 0x7fa54b396fd0>
print(type(obj))#output: <class '__main__.A'>
print(obj.x)


