
while 1:
    try:
        num1 = int(input("Enter First number.\n"))
        break
    except Exception as e:
        print("You entered wrong input :",e)
while 1:
    try:
        num2 = int(input("Enter Second number.\n"))
        sum = num1 + num2
        print("The sum =",sum)
        break
    except Exception as e2:
        print("You entered wrong input :", e2)

print("Thank you for the correct input.")


"""try:
    num1 = int(input())
    num2 = int(input())
    print(num1 + num2)
except Exception as e:
    print(e)

print("Thank you for your time .")"""


"""while True:
    try:

        num1 = int(input("Enter 1st no:"))

    except Exception as e:

        print("You entered wrong input:", e)

        continue

    break

while True:

    try:

        num2 = int(input("Enter 2nd no:"))

    except Exception as e2:

        print("You entered wrong input:", e2)

        continue

    break

print("The sum =", num1+num2, "Thank you for your correct input!")

#Nice ide"""

"""while True:

    try:

        print('Enter num1.')

        num1 = int(input())

        print('Enter num2.')

        num2 = int(input())

        print('The sum =',num1+num2)

        break

    except Exception as e:

        print('You entered wrong input',e)

print('Thank you! For your correct input.')"""