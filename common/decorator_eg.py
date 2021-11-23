"""
Creating own decorator and using it
"""




def normal_func():
	print("Executing Normal Function")



def decorator_func(a):
	print("Executing decorator function")



@decorator_func
def normal_func1():
	print("Executing Normal FUnction1")


if __name__ == "__main__":
	normal_func()
	normal_func1()