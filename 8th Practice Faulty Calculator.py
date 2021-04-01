# 45 * 3 = 55 , 56 + 9 = 77 , 56 / 6 = 4

op = ["+","-","*","/"]

print("Enter First number")
num1 = float(input())
print("Enter an operator",op)
opr = input()
print("Enter Second number")
num2 = float(input())
correction = ""
if correction == "Y":
    choice = input("Perss \"Y\" to Continue And \"N\" to Exit")
    #correction = choice.upper()
    if num1 == 45 and opr == "*" and num2 == 3 :
        print(55)
    elif num1 == 56 and opr == "+" and num2 == 9 :
        print(77)
    elif num1 == 56 and opr == "/" and num2 == 6 :
        print(4)
    elif opr == "+":
        ans = num1 + num2
        print(ans)
    elif opr == "-":
        ans = num1 - num2
        print(ans)
    elif opr == "*":
        ans = num1 * num2
        print(ans)
    elif opr == "/":
        ans = num1 / num2
        print(ans)
    else:
        print("Wrong input.")
else:
    print("Thank you !")