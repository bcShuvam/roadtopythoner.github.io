var = "Global" # Global variable

def funct1(n):
    """Global variables  value cannot be changed locally"""
    global var # It is a method to globalize a local variable
    var = "Local"# Local variable
    print(var)
    print(n,"Hello !")

funct1("Shuvam B.C")
print(funct1.__doc__)
print(var)

def harry():
    x = "harry"
    def rohan():
        global x
        x = "Rohan"
    print("before calling rohan()",x)
    rohan()
    print("before calling rohan()",x)

harry()
print(x)