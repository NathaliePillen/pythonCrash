import json

numbers = [2,4,6,8,10]

filename = 'numbers.json'
with open (filename, 'w') as file_object:
    json.dump(numbers, file_object)

filename = 'test.json'

letters = ['a','b','c','d','e','f']

with open (filename, 'w') as file_object:
    json.dump(letters, file_object)
    
    
    