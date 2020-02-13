prompt = "\nTell me something and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program"

active = True
while active:
    message = input(prompt)
    if message =='quit':
        active = False
    else:
        print (message)
        
prompt = "\nPlease enter a city that you've visited."
prompt += "\nEnter 'quit' to leave the program."

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(city)
        



        

    

