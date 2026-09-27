#write a program to find whether a user name contains lass then 10 characters or not

user_name = input("Enter your username: ")

if len(user_name) < 10:
    print("Your username contains less than 10 characters.")    

else:
    print("Your username contains more than 10 characters.")

