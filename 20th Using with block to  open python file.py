with open("Seek Tell More.txt") as f:
    a = f.readlines()
    print(a)

f = open("Seek Tell More.txt")
print(f.readlines())
f.close()