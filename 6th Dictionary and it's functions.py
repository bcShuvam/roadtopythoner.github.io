"""
Method 	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

# Dictionary is a key value pairs

list1 = []
print(type(list1))
tp = ()
print(type(tp))
dict1 = {}
print(type(dict1))

dict2 = {"Harry":26,
         "Rohan":22,
         "SkillF":18,
         "Shuvam":{"age":18,"Lives in":"Biratnagar-7,Hatkhola","Studies at":"Shikxadeep,class-12"}
         }
print(dict2)
dict2["Ankit"] = "Iphone"
dict2["Ujjwal"] = "SubgM" # It is a metho to add/update any new key with it's value the dictionary
dict2.update({"Leena":"Lollypop"}) # It is a metho to add/update any new key with it's value the dictionary
print(dict2.keys()) # It is a method to print the keys in the dictionary
print(dict2.items()) # It is a method to print the items of the key value in the dictionary
del dict2["Ankit"] # It is a method to delete any key with it's value
print(dict2)
print(dict2["Shuvam"]) # This a method to get value/items of the key
print(dict2.get("Shuvam")) # This is also a method to get value/items of the key
print(dict2.popitem())
dict2.pop("Harry")
print(dict2)

# d3 = dict2 This is a wrong method to copy
d3 = dict2.copy() # This a method to copy any container items without affecting the original container
del d3["Shuvam"]
print(d3)
print(dict2.clear()) # It is a method to clear/delete keys and items inside the container without deleting the container
del dict2 # It is a method to completely delete a container including it's keys and items
print(dict2)