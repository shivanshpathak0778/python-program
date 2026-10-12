# created a class (2 D vector) and use it to created anthor class representing a (3 D vector)

class TowDVetor:
    def __init__(self, i , j):
        self.i = i
        self.j = j 
        

    def show(self):
        print(f"the vetor is {self.i}i + {self.j}j")

class ThreeDVetor(TowDVetor):

    def __init__(self, i , j , k):
        super().__init__(i , j)
        self.k = k

        
    def show (self):
             print(f"the vetor is {self.i}i + {self.j}j + {self.k}k")
     
                
a = TowDVetor ( 1 , 2 )
a.show()
b = ThreeDVetor (1 , 2 , 3 )
b.show()         