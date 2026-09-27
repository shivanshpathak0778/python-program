# write a program  to find out whether a student is pass or fail; if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as input from the 

marks1= int(input("Enter marks for subject 1: "))
marks2= int(input("Enter marks for subject 2: "))   
marks3= int(input("Enter marks for subject 3: "))

# calculate totaal_percentage

total_marks =(100) * (marks1 + marks2 + marks3)/ 300

if total_marks >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:

    print("Congratulations! You have passed the exam.")
else:
    print("Sorry! You have failed the exam.")