# write a program to print the star

n = int(input("enter the number: "))
for i in range (1, n+1):
    print(" " * (n-i),end="")
    print("*"* (2*i-1),end="")
    print ("")
