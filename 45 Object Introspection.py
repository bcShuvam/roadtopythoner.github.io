class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    @property
    def email(self):
        return f"{self.fname}_{self.lname}@gmail.com"

skillF = Employee("Shuvam","BC")
print(skillF.email)
print(type(skillF))
print(id(skillF))
print(dir(skillF))

import inspect
print(inspect.getmembers(skillF))