"""
ref link : https://www.youtube.com/watch?v=NAQEj-c2CI8&ab_channel=TechWithTim
"""

#regular way of creating class
class RegularClass:
    pass

#behind the scenes (type constructor is called in which classname, base class names, parameters are passed)
NewClass = type("NewClass",(),{})

print(RegularClass) #output: <class '__main__.RegularClass'>
print(type(RegularClass)) #output: <class 'type'>



print(NewClass) #output: <class '__main__.NewClass'>
print(type(NewClass)) #output: <class 'type'>
print(NewClass.__subclasses__()) #output: [] #nosubclasses



"""
CLasses are objects in python
ANd, classes are of type type
i.e the class is an instance of type
"""
