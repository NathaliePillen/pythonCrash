filename = 'text_files/guest_book.txt'
print("Enter 'quit' when you want to leave the programm.")

while True:
    name = input("\nPlease fill in your name: ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
            print("Hi " + name + ", you've been added to the guest book.") 

