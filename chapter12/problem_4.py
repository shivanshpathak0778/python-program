# write a program to display a/b wher a and b are integers.
# display infinty error in o figur   

try:
    a = int (input("enter a: "))
    b = int (input("enter b: "))
    print(a/b)

except ZeroDivisionError as v:
    print("infinty")   