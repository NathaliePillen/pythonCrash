import json

numbers = [2,4,6,8,10]

filename = 'numbers.json'
with open (filename, 'w') as file_object:
    json.dump(numbers, file_object)
    
    
    