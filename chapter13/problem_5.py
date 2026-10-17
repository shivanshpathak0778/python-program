
from functools import reduce
l = [1,2,55,99,66,80,62,500,778,645,622,627]

def greater (a, b):
    if (a>b):
        return a
    return b
print(reduce(greater, l))