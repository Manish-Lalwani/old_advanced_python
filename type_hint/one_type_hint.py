"""
TYpe Hinting
ref link : https://medium.com/depurr/python-type-hinting-a7afe4a5637e

"""

#Basic Variables
# length    #just declaring variable without defining will give error
length: int #no error will be given

#with type hinting it is possible to just declare the variable without assigning value(that is without defining)
is_square: bool
width: bool
name: str

#for built in data structures like : list,dict,tuples, sets
from typing import List, Dict, Tuple, Set, Any, Optional, Union
l1: List[int]
#l1 = []
#print(hex(id(l1)))
# print(__dict__)

#l1 =[2,"a"] #one_type_hint.py:23: error: List item 1 has incompatible type "str"; expected "int"
l1 = [1]
l2 = []
l2 = [1]

print("\n\nDir",dir()) #lists all the variables defined
print("\n\nGlobals",globals())
print("\n\nLocals",locals())
print(f"type of l1 {type(l1)}, type of l2 {type(l2)}")


d1: Dict[str, str]
d2: Dict[Any, Any]

# d1[1] = "abc"



def f1(num1: int, name: str) -> str:
    print("num1 is",num1)
    print("name",name)

    return name


def f2(list1: List[str], list2: List[int]) -> List[Any]:
    print(f"List1 is {list1}")
    print(f"List2 is {list2}")
    return list1


def f3(dict1:Dict[int,Any]) -> Optional[int]:
    print("f3")
    return None

def f4(a=Union[int,float,str]) -> Optional[Any]:
    print(a)
    return None

from typing import Generic,TypeVar


class Demo:
    def __init__(self):
        print("INside INit Demo")


obj1:Demo




def f5(n1:num,)

"""
Additional Conclusion/Note: Just declaring the variables using type hinting does not allocates any memory on heap we can check using dir()
"""