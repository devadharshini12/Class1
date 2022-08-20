class Person(object):
 
    def __init__(self, name, id):
        self.name = name
        self.id = id
 
    def display(self):
        print(self.name)
        print(self.id)
        print(self.salary)
        print(self.designation)
 
 
class Employee(Person):
    def __init__(self, name, id, salary, designation):
        self.salary=salary
        self.designation=designation
        Person.__init__(self, name, id)

        
a = Employee('Dharshini',4141123,600000,"Developer")
a.display()
