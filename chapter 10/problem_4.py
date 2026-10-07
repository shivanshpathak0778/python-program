# add a static method in problem 2 ,to greet the use with hello

class calculater:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"the square of {self.n*self.n}")

    def cube(self):
            print(f"the cube of {self.n*self.n*self.n}")
        

    def squareroot(self):
            print(f"the square root of {self.n**1/2}")

    @staticmethod
    def helo ():
          print ("helo world")

a = calculater(4)
a.square()
a.cube()
a.squareroot()
a. helo ()