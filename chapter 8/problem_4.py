# write a python function to find the sum of natural numbers using recursion

def sum (n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
print(sum(4))