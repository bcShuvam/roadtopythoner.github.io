list1 = ["Harry","Larry","Carry","Marie"]

for item in list1:
    print(item)

list2 = ["Apple",9,1,7,3,"Cat",4,6,8,2,5,"Ball"]

for items in list2:
    if str(items).isnumeric() and items > 6:
        print(items)

dict1 = {"Harry":14,
         "Larry":15,
         "Carry":17,
         "Marie":19
         }

for names, ages in dict1.items():
    print(names,"\b's age is",ages)