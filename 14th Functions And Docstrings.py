a = 5
b = 10
c = sum((a , b)) # This is built in function for addition
print(c)

def function1(x ,y):
    print("This is how function works",sum((x, y)))

print(function1(5,7))
function1(5,7)

def funct2(m,n):
    # sum is a built in function used for addition
    average = sum((m , n))/2
    # print(average)
    return average

print(funct2.__doc__)
"""z = funct2(5,25)
print(z)"""