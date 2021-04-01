# divisible = []
# for i in range(100):
#     if i%3 == 0:
#         divisible.append(i)
#
# print(divisible)
#
# ls = [i for i in range(100) if i%2==0]
# print(ls)
#
# dict1 = {i:f"item {int(i/3)}" for i in range(30) if i%3 == 0}
# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n",dict2)
#
# dresses = {dress for dress in ["dress 1","dress 2","dress 1","dress 2"]}
# print(dresses)
#
# evens  = (i for i in range(100) if i%2==0)
# # print(evens.__next__())
# # print(evens.__next__())
# # print(evens.__next__(),"\n")
#
# for item in evens:
#     print(item)
ls = []
dict1 = {}
s = set()

dicti = {1:"list comprehension",2:"Dictionary comprehension",3:"Set comprehension"}
print("Select a format.")
for key, items in dicti.items():
    print(f"{key} : {items}")

while 1:
    try:
        select_format = int(input())
        break
    except Exception as e:
        print(f"Wrong Input {e} \nPlease! give input as an integer")

print(f"Enter number of item you want to add in \"{dicti.get(select_format)}\".")
while 1:
    try:
        no_of_items = int(input())
        break
    except Exception as e:
        print(f"Wrong Input {e} \nPlease! give input as an integer")

print(f"Enter any {no_of_items} items.")
if select_format == 1:
    for i in range(no_of_items):
        items_input = input()
        ls.append(items_input)
elif select_format == 2:
    for i in range(no_of_items):
        items_input = input()
        dict1.update({i:items_input})
        i += 1
# elif select_format == 3:
#     s.append(items_input)

print(dict1)
