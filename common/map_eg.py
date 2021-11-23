#The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.


# list example
l1 = [1,2,3,4,5,6]

def f1(num):
	"""RETURNS SQUARE OF THE PASSED NUMBER"""
	return num*num
l2 = map(f1,l1)

l3 = list(l2)
print(l1)
print(l2,type(l2))
print(l3)





