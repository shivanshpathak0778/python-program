# guess the currectly number

import random
n = random.randint(1 , 100)
a = -1
guess = 1
while(a != n):
    a = int(input("guess the currect number: "))
    if(a>n):
        print("lowe number plese ")
        guess +=1

    elif(a<n):
         print("higher number plese ")
         guess +=1
print(f"you have gaesed the {n} currectly in {guess} attempts")    





        

        







