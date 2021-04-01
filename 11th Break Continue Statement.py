while(1):
    list1 = ["+", "-", "*", "/"]
    print("Enter 1st number")
    num1 = float(input())
    print("Enter an arithmatic operation", list1)
    op = input()
    print("Enter 2nd number")
    num2 = float(input())

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("Wrong input")
    print("\n \bPress 1 to continue and 0 to exit")
    user = int(input())
    if user == 1:
        continue
    else:
        break