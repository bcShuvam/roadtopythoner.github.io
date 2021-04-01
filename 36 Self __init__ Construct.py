class Employee:
    no_of_leaves = 8
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    # def printdetails(self):
    """
    Normal class function dose not take argument
    """
    #     return f"Name is {self.name} , Salary is {self.salary} and role is {self.role}"

# harry.name = "Harry"
# harry.salary = 44444
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 33333
# harry.role = "Worker"

harry = Employee("Harry" , 5555 , "Teacher")
rohan = Employee("Rohan" , 44444 , "Worker")

print(harry.salary)
print(rohan.name)
print(rohan.role)