# Compare the contents of file2.txt and file3.txt

with open ('file2.txt', 'r') as f:
    content2 = f.read()


with open ('file3.txt', 'r') as f:
    content3 = f.read()

if content2 == content3:
    print("The contents of file2.txt and file3.txt are the same.")    

else:
    print("The contents of file2.txt and file3.txt are not the same.")    
