with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    
file_name = 'text_files/pi_million_digits.txt'
with open (file_name) as file_object:
    lines = file_object.readlines()
    
    pi_string = ''
    for line in file_object:
        pi_string += line.rstrip()        
        
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi")
else:
    print("Your birthday doesn't appear")
