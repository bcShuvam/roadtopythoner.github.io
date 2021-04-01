class A:
    classvar1 = "I'm a class variable in class A"
    def __init__(self):
        self.var1 = "I'm inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"
class B(A):
    classvar1 = "I'm in class B"
    def __init__(self):
        self.var1 = "I'm inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()


a = A()
b = B()

print(b.special,b.var1 ,b.classvar1)