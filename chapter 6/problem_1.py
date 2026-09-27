#write a program ot find the greatest of number entered by the user

a1= int(input("Enter a1 number:a1 "))
a2= int(input("Enter a2 number:a2 "))
a3= int(input("Enter a3 number:a3 "))

if a1>a2 and a1>a3:
    print("The greatest number is: a1 ", a1)
elif a2>a1 and a2>a3:
    print("The greatest number is: a2 ", a2)
else:
    print("The greatest number is: a3 ", a3)

