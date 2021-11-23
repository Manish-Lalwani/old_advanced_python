
#Regular Class
class A:
    def __init__(self,num1):
        self.num1 = num1

    def dunder_printer(self): #prints all dunder properties
        dunder_function_list = dir(self)
        print(dunder_function_list,type(dunder_function_list))
        print(f"printng self.__class__ {self.__class__}")
        for x in dunder_function_list:
            str1 ="print(self."+str(x)+")"
            #str1 = """print(self.__class__)"""
            print(str1[6:-1])
            exec(str1)
            print("\n")
    





if __name__ == "__main__":
    obj1 = A(num1=5)
    print("Object of Regular Class A created")
    print(f"__dict__ of obj1: {obj1.__dict__}")
    #print(dir(obj1))
    print(obj1.dunder_printer())
