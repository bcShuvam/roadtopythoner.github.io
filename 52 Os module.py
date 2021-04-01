import os

# print(dir(os))
print(os.getcwd()) # It is used to print the current working directory
# os.chdir("E://") # It is used to change the directory
# print(os.getcwd())

print(os.listdir("C://")) # It is used to list the folder and file in the directory
# os.mkdir("Os") # It is used to make single folder in the directory
# os.makedirs("Os/Oss/Osss") # It is used to make folder and its child folder and grandchild folder and so on
# os.rename("Os","oops") # It is used to rename any file and folder
print(os.environ.get('Path')) # It is used to print enviroment variable

print(os.path.join("E://","path_join.txt"))
print(os.path.exists("E://Zoom"))
print(os.path.isfile("E://Zoom"))
print(os.path.isdir("E://Zoom"))