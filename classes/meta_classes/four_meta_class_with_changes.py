    """
Metaclass with changes
"""

class Meta(type): #this the meta class which inherits the type class
    def __new__(cls,class_name,base,attr): 
        print("passed attributes",attr)
        modified_attr = {}

        for x,y in attr.items():
            if x.startswith("__"): #if dunder methods no change
                modified_attr[x] = y
            else:               #else will rename the variable and function name to upper case
                modified_attr[x.upper()] =y
        print("modified attributes", modified_attr)
        return super().__new__(cls,class_name,base,modified_attr) #calling type __new__method and pasing the modified attributes


#this is normal class we are creating but we have specified metaclass= Meta so it will be created as normal class but the call will be go through meta class and the changes which we have mentioned in the class will be applied and than only the call will be given
class A(metaclass=Meta):
    x=5
    y=6
    
    def function1(self):
        print("hi")




obj = A()
#print(obj.x) #attribute error, as we changed the variable and method to uppercase
print(obj.X)



