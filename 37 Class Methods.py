class Employee:
    no_of_leaves = 8
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name} , Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls , newleaves):
        cls.no_of_leaves = newleaves

harry = Employee("Harry" , 5555 , "Teacher")
rohan = Employee("Rohan" , 44444 , "Worker")

inp = int(input("Enter number of leaves\n"))
print("Before change leaves =",harry.no_of_leaves)
harry.change_leaves(inp)
print("After change leaves =",Employee.no_of_leaves)
