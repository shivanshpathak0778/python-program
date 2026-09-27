#write a program to check a given name is present in the list of names or not

names_list = ["Shivansh", "Aman", "Deep", "Preet", "Ekansh"]
input_name = input("Enter a name to check: ")

if input_name in names_list:
    print("The name is present in the list.") 
else:
    print("The name is not present in the list.")