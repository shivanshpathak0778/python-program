# write a program to takeout the lenth of vector  

class vector:
    def  __init__(self , l):
        self.l = l


    def __len__(self):
        return len(self.l)    


v1 = vector([1 ,4 ,5 ,9])
print (len(v1))    