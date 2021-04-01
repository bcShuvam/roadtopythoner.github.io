# def funct_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)
#
# funct_name_print(cc)

def funct(normal_argument,*args,**kwargs):
    print(type(args))
    print(normal_argument)
    for items in args:
        print(items)
    for key,value in kwargs.items():
        print(f"{key} is a {value}.")

user_name = ["Hari","Shyam","Shivam","Harry","Rohan","Riya","Ram"]
normal_argument = "Normal argument can only be passed as the first argument in functions"
kw = {"Shuvam":"Programmer",
      "Yuvarj":"Hacker",
      "Manish":"Road Engineer",
      "Mia":"Bitch"
     }
funct(normal_argument,*user_name,**kw)