filename='text_files/personal.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())   

with open(filename) as file_object:
    lines=file_object.readlines()
textstring = ''
for line in lines:
    textstring += line.rstrip()
print(textstring)
     
        