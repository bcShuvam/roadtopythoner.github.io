
def factorial_iterative(n):
    """

    :param n:
    :return: n * n -1 * n - 2 * n-3 ...... 1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

number = int(input("Enter a number : "))
print("factorial using iterative method",factorial_iterative(number))

def factorial_recursive(n):
    """
    5 * factorail_recursive(4)
    5 * 4 * factorail_recursive(3)
    5 * 4 * 3 * factorail_recursive(2)
    5 * 4 * 3 * 2 * factorail_recursive(1)
    5 * 4 * 3 * 2 * 1 = 120
    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print("factorial using recursive method",factorial_recursive(number))

def fibonacii(n):
    """

    :param n:
    :return: 0 , 0+1 = 1 , 1+2 = 3 , 2+3 = 5 , 3+5 = 8 , 4+8 = 12
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacii(n-1) + fibonacii(n - 2)

fibonacii_input = int(input("Enter a number : "))
print(fibonacii(fibonacii_input))