# write a program to check a spam

p1 = "make a lot of money"
p2 = "buy now"
p3 = "click here"

input_message = input("Enter a message: ")

if p1 in input_message or p2 in input_message or p3 in input_message:
    print("This message is spam.")

else:
    print("This message is not spam.")