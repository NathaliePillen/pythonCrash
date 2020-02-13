#ex1
prompt = "\nGeef hier je toppings in: "
prompt += "\nEnter 'quit' om het programma te verlaten"

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message + "zijn jouw pizza-toppings")
        
#ex2


#ex3
prompt = "\nWat is jouw leeftijd? "
prompt += "\nquit om het programma te verlaten"
    
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        message = int(message)
        if message < 3:
            print('Gratis')
        elif message < 12:
            print('Ticket is 10 euro')
        else:
            print('Ticket is 15 euro')
        
    