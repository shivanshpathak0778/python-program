# write a program to find the greatest number using function


def greatest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

    
a = 10
b = 5   
c = 3
print(greatest_number(a, b, c)) 