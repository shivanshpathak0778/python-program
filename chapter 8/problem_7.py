# write a python program to remove an item from a list

def ram (l,word):
    for item in l:
        l.remove(word)
        return l
   

l = ["aman", "shivansh", "rahul"]

print(ram(l, "rahul"))