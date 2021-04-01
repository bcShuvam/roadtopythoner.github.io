a = input("What is your name : ")
b = input("How much do you earn : ")

if int(b) == 0:
    raise ZeroDivisionError("b is 0 so stopping the program")

if a.isnumeric():
    raise Exception("Numbers are not allowed")

print(f"Hello! {a}")

# a = [6 , 4 , "34"]
# b = [6 , 4 , "34"]
# print(a is b)