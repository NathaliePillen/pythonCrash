import json

filename = 'numbers.json'
with open (filename) as file_object:
    numbers = json.load(file_object)

print (numbers)

username = input("What is your name? ")

filename = 'username.json'

with open (filename, 'a') as file_object:
    json.dump(username, file_object)

    
    
    
    
    