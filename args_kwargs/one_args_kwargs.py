#ref link https://www.geeksforgeeks.org/args-kwargs-python/
#Using the *, the variable that we associate with the * becomes an iterable meaning you can do things like iterate over it, run some higher-order functions such as map and filter, etc.
def m1(*args):
    print(f"Type of args is:{type(args)} ")
    print("Arguments passed are")
    for x in args:
        print(x)

def m2(**kwargs):
    print(f"Type of kwargs is:{type(kwargs)}")
    print("Arguments passed are")
    for x,y in kwargs.items()   :
        print(x,y)
        

def m3(*args,**kwargs):
    print("Have passed both args and kwargs")
    print("Printing all args argument")
    for x in args:
        print(x)
    print("-------------------------")
    print("Printing all kwargs argument")
    for x,y in kwargs.items():
        print(x,y)



if __name__ == "__main__":
    m1("a","b","c","d","e") #*args
    print("\n*********************")
    m2(height=10,width=20,radius=6)
    print("\n**********************")
    m3("1","2","3","4",height="10",width="20")
    #m3(height="10", width="20", "1", "2", "3") #gives error positional argument after keyword argument
    #m3("1", "2", "3", height="10", width="20","4") #gives error positional argument after keyword argument
