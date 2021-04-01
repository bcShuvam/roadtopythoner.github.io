"""
Method 	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

# List
#List value can be changed / it's Mutable

grocery = ["Harpic","Vim bar","deodrant","Bhindi","Lollypop",56]
print(grocery[1:5:2])
print(len(grocery)) #It shows the total lenght/index of the list
print(grocery)
grocery.append("Samosa")
grocery.append(12) # It is used to add item at the end of the list
grocery.insert(1,"Laddu") # It is used to insert/add item at a specific index
grocery.remove(12) # It is used to remove any item from the list by writing it's name
grocery.pop() # IT is used to remove last item from the list
print(grocery)


numbers = [2,5,1,4,9,7]
print(min(numbers))# It shows lowest value number number is the list
print(max(numbers))# It shows highest value number in the list
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers[1] = "add me" # It is also a method to add item to the list
print(numbers)

"""
Tupel
Mutable = It's value can be changed
Immutable = It's value cannot be changed
Method 	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""

# Tuple example
# Tuple value cannot be changed / It's Immutable

tupleee = (1,3,5)
# tupleee[1] = 9 #It
print(tupleee)

tp = ("To make a tuple atleast 1 item with a "," should be created",)
# tp[1] = 2
print(tp)

a = 1
b = 5
a , b = b , a # It is method to exchange value of any container
"""
c = a
a = b
b = c
This is a traditional method to exchange value
"""
print(a,b)