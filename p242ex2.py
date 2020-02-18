filename = "text_files/preferences.txt"
print("Enter 'quit' when you want to leave the programm.")

while True:
    name = input ('why do you like programming? ')
    if name == 'quit':
        break
    else:
        with open (filename, 'a') as file_object:
            file_object.write(name + "\n")
    print ("These are the reasons why people like programming: " + name)

with open(filename) as file_object:
    content = file_object.read()
    print(content)


