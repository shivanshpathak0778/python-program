#creat a class "programing" for storing informations of few programings working at microsoft.

class program:
    compny = "microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

self = program("shivansh", 5000, 1234)

print(self.name)
print(self.salary)
print (self.pin)
print(self.compny)