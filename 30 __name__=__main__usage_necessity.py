# 30 __name__=__main__usage_necessity
def printshuv(string):
    return f"Hello {string}"

def add(num1,num2):
    return num1 + num2 + 5

print("And the name is",__name__)
if __name__ == '__main__':
    print(printshuv("Shuvam BC !"))
    o = add(4,6)
    print(o)