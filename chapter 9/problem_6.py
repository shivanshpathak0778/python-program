# write a program to check if the word 'python' is present in a file or not.

with open('file3.txt', 'r') as f:
    content = f.read()

if 'python' in content:  
    print("The word 'python' is present in the file.")
  
else:
    print("The word 'python' is not present in the file.")    