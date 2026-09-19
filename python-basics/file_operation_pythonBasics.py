'''
Reading data from a file
'''
print('====================Reading data from a file=============================')

with open("./files/example.txt",'r') as file:
    content = file.read()
    print(content)

print('====================Reading data from a file=============================')



print('====================Reading data line by line from a file=============================')

with open('./files/example.txt','r') as file:
    for line in file:
        print(line.strip()) # strip removes the newline character

print('====================Reading data line by line from a file=============================')



print('====================writing to a file(overwriting)=============================')

with open('./files/example.txt','w') as file:
    file.write("Hello world \n")
    file.write("this is new line")

print('====================writing to a file(overwriting)=============================')



print('====================writing to a file(not overwriting)=============================')

with open('./files/example.txt','a') as file:
    file.write("\nAppead operation taking place \n")
    file.write("this is new line \n")

print('====================writing to a file(not overwriting)=============================')


'''
writing list of lines to a file
'''
print('====================writing list of lines to a file=============================')

lines = ["first line \n","second line \n", "third line \n"]
with open('./files/example.txt','a') as file:
    file.writelines(lines)

print('====================writing list of lines to a file=============================')



'''
Reading content from source file and writing to destination file
'''
print('====================Reading content from source file and writing to destination file=============================')

with open('./files/example.txt','r') as source_file:
    content = source_file.read()

with open("./files/destination_example.txt",'w') as destination_file:
    destination_file.write(content)

print('====================Reading content from source file and writing to destination file=============================')



'''
Todo
Read a file and count no of lines , words , characters
'''




'''
create new Directory
'''
print('====================create new Directory=============================')

import os
directory_path = './files/packages'
# os.mkdir(directory_path)
print(f"Directory '{directory_path} created'")

print('====================create new Directory=============================')



'''
Listing files and directories
'''
print('====================Listing files and directories=============================')

items = os.listdir("./files")
print(items)

print('====================Listing files and directories=============================')




'''
Joining Paths
'''
print('====================Joining Paths=============================')

dir_name = "/files/packages"
file_name = "file.txt"
full_path = os.path.join(os.getcwd(), dir_name , file_name)
print(f"full path : {full_path}")

print('====================Joining Paths=============================')




'''
check file path exists
'''
print('====================check file path exists=============================')

path = "./files/example.txt"

if os.path.exists(path):
    print(f"the path {path} exists")
else:
    print(f"the path {path} not exists")

print('====================check file path exists=============================')



'''
check if it is a file or directory
'''
print('====================check if it is a file or directory=============================')

path = "./files/packages/example.txt"

if os.path.isfile(path):
    print(f"the path {path} is a file")
elif os.path.isdir(path):
    print(f"the path {path} is a directory")
else:
    print(f"the path {path} is neither directory nor file")

print('====================check if it is a file or directory=============================')