# file_handel = open("Writing And Appending.txt","w")
# count = file_handel.write("It will create a text if not exist.\n")
# print(count)
#
# file_handel.close()

#
f = open("Reading And Writing.txt","r+")
f.write("r+ is used for reading and writing a file .\n")
f.write("It will throw an error if the file doesn't exist\n")
f.write("To use r+ , The file must exist.\n")
# print(f.readline())

for line in f:
    print(line,end="")

f.close()