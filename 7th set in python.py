s = set()
print(type(s))
s.add(1)
s.add(2)
#s1 = s.union({1,2,3})
s1 = s.intersection({1,2,3})
print(len(s1))
s.remove(1)
print(s,s1)

l = [6,7,8,9]
set_from_list2 = set(l)
set_from_list = set([1,2,3,4,5])
print(set_from_list)
print(type(set_from_list2))

"""
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""