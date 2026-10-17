# store the multiplcation tables generated in problem 3 in a file named tables .txt 



n = int(input("enter your number: "))

table = [n*i for i in range (1, 11)]
with open ("table.txt","a")as f:
    f.write(str(table)+"\n")


