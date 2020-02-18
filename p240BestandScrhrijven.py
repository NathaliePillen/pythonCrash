filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    
with open(filename) as file_object:
    content = file_object.read()
    print(content)
    
with open(filename, 'a') as file_object:
    file_object.write('I love to eat some pizza.\n')

with open(filename) as file_object:
    content = file_object.read()
    print(content)
    
