""""
Creating class with Type and adding function to it

As in python functions are also object,therefore they are passed as parameter to type
"""
#regular class creation
class RegularClass:
    x =5

    def f1(self):
        print("Regularlass f1 function")

def f1(self):
    print("inside f1 function")

#using type
NewClass = type("NewClass",(),{"x":5,"f1":f1}) #here while creating class using type have also passed x as a variable and f1 as function



nc_obj = NewClass()
rc_obj = RegularClass()


print(f"\nRegularClass: {RegularClass}")
print(f"rc_obj: {rc_obj}, rc_obj.x: {rc_obj.x}\n")

print(f"NewClass: {NewClass}")
print(f"obj: {nc_obj}, nc_obj.x: {nc_obj.x}\n")



