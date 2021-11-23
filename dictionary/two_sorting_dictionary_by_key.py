"""
Sorting dictionary keywise
"""

d1 = {
	5: 'a',
	3: 'z',
	1: 'd',
	2: 'g',
}

l1 = sorted(d1.items(),key=d1.get)
#print(l1)
for x in l1:
	print(x,':',d1[x])