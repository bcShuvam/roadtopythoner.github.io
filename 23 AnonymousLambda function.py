# Lambda functions or anonymous function
# Lambda function is a sort hand function

def add(a,b):
    return a + b

minus = lambda x, y : x - y

print(add(5,5))
print(minus(5,5))

def l_of_l_sort(a):
    return a[0]

l_of_l = [[1,4],[8,5],[2,23],[2,8],[1,10]]
l_of_l.sort(key=lambda x:x[1])
print(l_of_l)