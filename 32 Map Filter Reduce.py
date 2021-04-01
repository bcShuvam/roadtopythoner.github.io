numbers = ["3","34","64"]
######### Map Function #########
numbers = list(map(int , numbers))

def sq(a):
    return a*a

def cube(a):
    return a*a*a

# num = [2,3,5,25,7,4,9]

funct = [sq,cube]

for i in range(5):
    val = list(map(lambda x:x(i),funct))
    print(val)

# square = list(map(lambda x:x*x,num))
# print(square)
#
# cube = list(map(lambda c:c*c*c,num))
# print(cube)

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1
# print(numbers[2])

######### Filter Function ############
print("")

filter_list = [1,2,3,4,5,6,7,8,9]
def is_greater(num):
    return num>5

grt_than_5 = list(filter(is_greater,filter_list))
print(grt_than_5)


######### Reduce #########
from functools import reduce

list1 = [1,2,3,4]
sum = reduce(lambda x,y:x+y,list1)
product = reduce(lambda x,y:x*y,list1)
print(sum)
print(product)
# num = 0
# for i in list1:
#     num = num + i
# print(num)