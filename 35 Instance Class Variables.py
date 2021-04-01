class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 44444
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 33333
harry.role = "Worker"
print(rohan.no_of_leaves)
Employee.no_of_leaves = 9
print(rohan.no_of_leaves)
harry.no_of_leaves = 10
print(harry.no_of_leaves)