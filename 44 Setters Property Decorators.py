class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}_{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None and self.lname == None:
            return "Email is not set . Please set it using setter ."
        return f"{self.fname}_{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("Setting Now ...")
        names = string.split("@")[0]
        self.fname = names.split("_")[0]
        self.lname = names.split("_")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

supporter = Employee("Democracy","Supporter")

print(supporter.email)
supporter.fname = "Rajtantra"
print(supporter.email)
supporter.email = "Shuvam_Bc@gmail.com"
print(supporter.lname)

del supporter.email

print(supporter.email)
