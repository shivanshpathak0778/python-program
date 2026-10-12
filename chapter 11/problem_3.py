#Create a class 'Employee' and add salary and increment 
# properties to it.
# Write a method 'salaryAfterIncrement' method 
# with a @property decorator with a setter which changes 
# the value of increment based on the salary

class Employee:
    salery = 300
    increment = 20
    @property
    def saleryafterincrement(self):
        return (self.salery + self.salery * (self.increment/100) )
    
    @saleryafterincrement.setter
    def saleryafterincrement (self,salery):
        self.increment = ((salery/self.salery) -1)*100 
    
    
    
e = Employee()
# print(e.saleryafterincrement)
e.saleryafterincrement = 360.0
print(e.increment)

