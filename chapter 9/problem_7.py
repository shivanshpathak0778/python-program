# write a program to check if the word 'python' is present in a file or not and also print the line number where it is present.

with open('file3.txt', 'r') as f:
    lines = f.readlines()  

lineno = 1
for line in lines:
    if 'python' in line:
        print(f"The word 'python' is present in the file at line {lineno}.")
        break
    lineno += 1
else:
    print("The word 'python' is not present in the file.")