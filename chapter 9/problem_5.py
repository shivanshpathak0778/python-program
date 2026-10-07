# This code reads the content of a file named "file2.txt", replaces specific words in the content with "######", and then writes the modified content back to the same file. The words to be replaced are specified in the list `word`, which contains "shivansh", "aman", and "good".


word = ["shivansh", "aman", "good"]

with open("file2.txt", "r") as f:
    content = f.read()

new_content = content
for w in word:
    new_content = new_content.replace(w, "######")

with open("file2.txt", "w") as f:
    f.write(new_content)