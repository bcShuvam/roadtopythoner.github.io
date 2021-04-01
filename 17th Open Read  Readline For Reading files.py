file_pointer = open("File IO.txt","rt")
# content = file_pointer.read(300)
# print(content)
print(file_pointer.readline())
print(file_pointer.readlines()) # It is used to store lines in list

# for line in content:
#     print(line,end="")

file_pointer.close()