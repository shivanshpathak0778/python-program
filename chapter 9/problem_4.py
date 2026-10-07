# This script reads the content of a file named "file.txt", replaces all occurrences of the word "donkey" with "######", and then writes the modified content back to the same file.

word = "donkey"

with open("file.txt", "r") as f:
    content = f.read()

new_content = content.replace(word, "######")

with open("file.txt", "w") as f:
    f.write(new_content)