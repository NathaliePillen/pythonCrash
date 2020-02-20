import json
#load the username if it has been stored
#otherwise, prompt for the username and store it.

filename = 'username.json'

try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("Please fill in your name? ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print ("Hello " + username)
else:
    print("Welcome Back " + username)

    
    