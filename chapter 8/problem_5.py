# write a python function to print a pattern using recursion

def parten (n):
    if n == 0:
        return 0    
    print("*" * n)
    parten(n - 1)

parten(5)    