print("Enter a number from 1-9")
user_input = int(input())
print("Select either 0 or 1 to print star pattern")
user_choice = int(input())
convert = bool(user_choice)
print("\n")

if user_choice is True:
    for i in range(1,user_input):
        for j in range(1, i + 1):
            print("*",end=" ")
        print()

        # j -= i
        # print("*")

# num_rows = int(input("Enter the number of rows"));
# for i in range(0, num_rows):
#     for j in range(0, num_rows-i-1):
#         print(end=" ")
#     for j in  range(0, i+1):
#         print("*", end=" ")
#     print()