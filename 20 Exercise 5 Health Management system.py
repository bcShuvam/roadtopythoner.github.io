# import datetime
#
# user_name = ["Harry","Rohan","Hammad"]
# print(f"Press 1 to log \"{user_name[0]}\" , Press 1 to log \"{user_name[1]}\" and Press 1 to log \"{user_name[2]}\".")
# choose_name = int(input())
#
# def getdate():
#     return datetime.datetime.now()
#
# log_time = str(getdate())
#
# def harry_file():
#     print("Press 1 to \"Write\" and Press 2 to \"Retrieve\".")
#     write_retrieve = int(input())
#     if write_retrieve == 1:
#         harrys_file = open("harry.txt","a")
#         print("Press 1 to log \"Diet\" and press 2 to log \"Exercise\".")
#         to_do = int(input())
#         if to_do == 1:
#             print("Enter the diet which you have taken today .")
#             diet = input()
#             harrys_file.write(f"{log_time} : {diet}\n")
#         elif to_do == 2:
#             print("Enter the diet which you have taken today .")
#             exercise = input()
#             harrys_file.write(f"\n{log_time} : {exercise}\n")
#
#         harrys_file.close()
#     elif write_retrieve == 2:
#         harrys_file = open("harry.txt","r")
#         for data in harrys_file:
#             print(data)
#         harrys_file.close()
#
# def rohan_file():
#     print("Press 1 to \"Write\" and Press 2 to \"Retrieve\".")
#     write_retrieve = int(input())
#     if write_retrieve == 1:
#         rohans_file = open("rohan.txt", "a")
#         print("Press 1 to log \"Diet\" and press 2 to log \"Exercise\".")
#         to_do = int(input())
#         if to_do == 1:
#             print("Enter the diet which you have taken today .")
#             diet = input()
#             rohans_file.write(f"{log_time} : {diet}\n")
#         elif to_do == 2:
#             print("Enter the diet which you have taken today .")
#             exercise = input()
#             rohans_file.write(f"\n{log_time} : {exercise}\n")
#
#         rohans_file.close()
#     elif write_retrieve == 2:
#         rohans_file = open("rohan.txt", "r")
#         for data in rohans_file:
#             print(data)
#         rohans_file.close()
#
# def shuvam_file():
#     print("Press 1 to \"Write\" and Press 2 to \"Retrieve\".")
#     write_retrieve = int(input())
#     if write_retrieve == 1:
#         shuvams_file = open("shuvam.txt", "a")
#         print("Press 1 to log \"Diet\" and press 2 to log \"Exercise\".")
#         to_do = int(input())
#         if to_do == 1:
#             print("Enter the diet which you have taken today .")
#             diet = input()
#             shuvams_file.write(f"{log_time} : {diet}\n")
#         elif to_do == 2:
#             print("Enter the diet which you have taken today .")
#             exercise = input()
#             shuvams_file.write(f"\n{log_time} : {exercise}\n")
#
#         shuvams_file.close()
#     elif write_retrieve == 2:
#         shuvams_file = open("shuvam.txt", "r")
#         for data in shuvams_file:
#             print(data)
#         shuvams_file.close()
#
# if choose_name == 1:
#     harry_file()
# elif choose_name == 2:
#     rohan_file()
# elif choose_name == 3:
#     shuvam_file()
# else:
#     print("Wrong input")

# Health Management System

client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
lock_list = {1: "Exercise", 2: "Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input())
    print("Selected Client : ", client_list[client_name], "\n", end="")
    print("Press 1 for Lock")
    print("Press 2 for Retrieve")
    op = int(input())

    if op == 1:
        for key, value in lock_list.items():
            print("Press", key, "to lock", value, "\n", end="")

        lock_name = int(input())
        print("Selected Job : ", lock_list[lock_name])
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")
        k = 'y'

        while (k != "n"):
            print("Enter", lock_list[lock_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue

        f.close()

    elif op == 2:
        for key, value in lock_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        lock_name = int(input())
        print(client_list[client_name], "-", lock_list[lock_name], "Report :", "\n", end="")
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")
        contents = f.readlines()

        for line in contents:
            print(line, end="")

        f.close()

    else:
        print("Invalid Input !!!")

except Exception as e:
    print("Wrong Input !!!")