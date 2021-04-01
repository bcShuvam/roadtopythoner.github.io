"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -
"""

name = "Shuvam"
Iterator = iter(name)
print(Iterator.__next__())
print(Iterator.__next__())
print(Iterator.__next__())
print(Iterator.__next__())
print(Iterator.__next__())
print(Iterator.__next__())
# for c in name:
#     print(c,end="")

# print("Enter a number to print generated number")
# user_input = int(input())
# i = 1
# for i in range(user_input):
#     fact = user_input * (user_input - i)
#     print(fact)
#     i += 1

# print(factorical(user_input))