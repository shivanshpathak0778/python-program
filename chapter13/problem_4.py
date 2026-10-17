
def divisibles(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,55,99,66,80,62,500,7788,64582,62275,627413]
f = list(filter(divisibles,a))
print(f)
