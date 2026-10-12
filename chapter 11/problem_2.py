# create a class

class Animal:
    pass


class Pet (Animal):
    pass


class Dog (Pet):
    @staticmethod
    def brak():
        print("Bow Bow!")


d = Dog
d.brak()


    