# make a copy of file4.txt and save it as file_copy.txt

with open ('file4.txt', 'r') as f:
    content = f.read()

with open('file_copy.txt', 'w') as f:
    f.write(content)