# write a class "calculater" capable of calculating square, cube and square root of a number.

class calculater:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"the square of {self.n*self.n}")

    def cube(self):
            print(f"the cube of {self.n*self.n*self.n}")
        

    def squareroot(self):
            print(f"the square root of {self.n**1/2}")
    

a = calculater(4)
a.square()
a.cube()
a.squareroot()