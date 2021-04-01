# def searcher():
#     import time
#     book = "This is a book on harry and code with harry and good"
#     time.sleep(3)
#
#     while True:
#         text = (yield )
#         if text in book:
#             print("Your text is in the book")
#         else:
#             print("Text is not in the book")
#
# search = searcher()
# print("Search started")
# next(search)
# search.send("harry")
# input("Press any key : ")
# search.send("book")
#
# search.close()
def search_name():
    import time
    lst = ["Shuvam","Harry","Rahul","Jhon","Rock","KO"]
    info = {
        "Shuvam":1234567890,
        "Harry":2345678901,
        "Rahul":3456789012,
        "Jhon":4567890123,
        "Rock":5678901234,
        "KO":6789012345
    }
    time.sleep(2)

    # while True:
    #     name = (yield )
    #     if name in lst:
    #         x = lst.index(name)
    #         print(f"Name \"{user_name}\" found on index {x+1}.")
    #     else:
    #         print(f"{user_name} not found.")

    while True:
        name = (yield )
        if name in lst:
            x = info.get(name)
            print(f"Name's \"{user_name}\" and  contact number is {info.get(user_name)}")
        else:
            print(f"{user_name} not found.")

search = search_name()
s_name = input("Search any name : ")
user_name = s_name.capitalize()
print(f"Searching ...")
next(search)
search.send(user_name)

search.close()