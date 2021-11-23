#filter example

l1 = [1,2,3,4,5,6,7,8,9,0]

l2 = filter(None,l1)

def divisiblity_two(number):
	if number%2 ==0:
		return True
	else:
		return False #if not return also still the filter will work

l3 = filter(divisiblity_two,l1)


print(list(l1))
print(list(l2))
print(list(l3))


#output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [2, 4, 6, 8, 0]
