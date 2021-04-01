class Constructor:
    def __init__(self,name,role,salary):
        self.name = name
        self.role = role
        self.salary = salary
    @classmethod
    def from_dash(cls,string):
        info = string.split("-")
        return f"Name : {info[0]}\nRole : {info[1]}\nSalary : {info[2]}"

    # @classmethod
    # def from_slash(cls, string):
    #     return cls(*string.split("/"))

print(Constructor.from_dash("Shuvam-Programmer-99999"))
# print(Constructor.from_slash("Motu/Student/00000"))