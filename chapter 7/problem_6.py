# # write a program calculate the factoral of agiven number using loop
 
n = int(input("enter youe number: "))
product = 1
for i in range (1, n+1):
       product = product * i
print (f"the factoral of {n} is {product}")
