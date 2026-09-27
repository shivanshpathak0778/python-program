#write a program to check the grade of a student based on the marks obtained

input_marks = int(input("Enter your marks: "))

if input_marks <= 100 and input_marks >= 90:
    print("Your grade is ex.")

elif input_marks < 90 and input_marks >= 80:
    print("Your grade is A.")    
elif input_marks < 80 and input_marks >= 70:
    print("Your grade is b.")    
elif input_marks < 70 and input_marks >= 60:
    print("Your grade is c.")    
elif input_marks < 60 and input_marks >= 50:
    print("Your grade is d.")    
elif input_marks < 50 :
    print("Your grade is f.")    
