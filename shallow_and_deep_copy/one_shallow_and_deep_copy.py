"""
Assignment, Shallow and deep copy
"""

import copy

l1 = [1,2,3,4,5,6]
print(f"l1 is {l1}, id of l1 {id(l1)}\n")
print("###############")
#Assignment
l2 = l1
l2[0] = -2
print(f"l1 is {l1}, id of l1 {id(l1)}\nl2 is {l2} id of {id(l2)}\n") ###only references changes the main list
print("###############")


l3 = copy.copy(l1)
l3[1] = 'shallowcopy'
print(f"l1 is {l1}, id of l1 {id(l1)}\nl2 is {l2} id of {id(l2)}\nl3 is {l3} id of {id(l3)}\n") ###creates a new object but for complex objects(internal objects will have reference)
print("###############")


l4 = copy.deepcopy(l1)
l4[5] = 'deepcopy'
print(f"l1 is {l1}, id of l1 {id(l1)}\nl2 is {l2} id of {id(l2)}\nl3 is {l3} id of {id(l3)}\nl4 is {l4} id of {id(l4)}\n")
print("###############")





#####shalow copy for complex objects##########
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]
l3 = [10,11,12,13,14,15]
l4 = [16,17,18,19,20]

l5 = [l1,l2,l3,l4]
print("l5 before assignment",l5)

l6 = copy.copy(l5)
l6[0][0] = 'shalow copy'

print(f"l5 is {l5}, id of l5 {id(l5)}\nl6 is {l6} id of {id(l6)}") #as said earlier shadow copies makes a copy of the outer object but for inner objects holds reference
print("###############")

print("original list:")
print(l5)
print([id(x) for x in l5])

print("shallow copy list")
print(l6)
print([id(x) for x in l6])







#####deepcopy for complex objects##########
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]
l3 = [10,11,12,13,14,15]
l4 = [16,17,18,19,20]

l5 = [l1,l2,l3,l4]
print("l5 before assignment",l5)

l6 = copy.deepcopy(l5)
l6[0][0] = 'shalow copy'

print(f"l5 is {l5}, id of l5 {id(l5)}\nl6 is {l6} id of {id(l6)}") #as said earlier shadow copies makes a copy of the outer object but for inner objects holds reference
print("###############")
	
print("original list:")
print(l5)
print([id(x) for x in l5])

print("deep copy list")
print(l6)
print([id(x) for x in l6])






###################################################################################################################
"""
(python3.6) xyz@JARVIS:~/practice/shallow_and_deep_copy$ python -i one_shallow_and_deep_copy.py 
l1 is [1, 2, 3, 4, 5, 6], id of l1 140477486464200

###############
l1 is [-2, 2, 3, 4, 5, 6], id of l1 140477486464200
l2 is [-2, 2, 3, 4, 5, 6] id of 140477486464200

###############
l1 is [-2, 2, 3, 4, 5, 6], id of l1 140477486464200
l2 is [-2, 2, 3, 4, 5, 6] id of 140477486464200
l3 is [-2, 'shallowcopy', 3, 4, 5, 6] id of 140477486447432

###############
l1 is [-2, 2, 3, 4, 5, 6], id of l1 140477486464200
l2 is [-2, 2, 3, 4, 5, 6] id of 140477486464200
l3 is [-2, 'shallowcopy', 3, 4, 5, 6] id of 140477486447432
l4 is [-2, 2, 3, 4, 5, 'deepcopy'] id of 140477486445448

###############
l5 before assignment [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
l5 is [['shalow copy', 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]], id of l5 140477486445448
l6 is [['shalow copy', 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]] id of 140477486809352
###############
original list:
[['shalow copy', 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
[140477486461384, 140477486461448, 140477486464200, 140477486447432]
shallow copy list
[['shalow copy', 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
[140477486461384, 140477486461448, 140477486464200, 140477486447432]
l5 before assignment [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
l5 is [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]], id of l5 140477486464712
l6 is [['shalow copy', 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]] id of 140477486445448
###############
original list:
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
[140477486462920, 140477486462088, 140477486461768, 140477486462728]
deep copy list
[['shalow copy', 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
[140477486120072, 140477486120456, 140477486120136, 140477486120392]
>>> exit()
(python3.6) xyz@JARVIS:~/practice/shallow_and_deep_copy$ 


"""

