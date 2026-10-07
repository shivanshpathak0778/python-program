# write aprogram to read the text from a given file pome .txt and fond out whether it contain the words "twinkle" or not.

f = open("poem.txt", "r")
content = f.read()

if "twinkle" in content:
    print("The word 'twinkle' is present in the poem.")

else:
    print("The word 'twinkle' is not present in the poem.")

f.close()        