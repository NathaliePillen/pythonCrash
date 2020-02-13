aliens = []

#voeg aan de lege lijst 30 aliens toe
for alien_number in range (30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

#print de eerste 5 aliens af
for alien in aliens[:5]:
    print (alien)

#print het aantal aliens
print ("Total number of aliens is " + str(len(aliens)))



pizza = {
    'crust': 'thick',
    'toppings' : ['extra cheese', 'mushrooms']
    }

print ("You orderd a " + pizza['crust'] + " crusted pizza with the following toppings: ")

for topping in pizza['toppings']:
    print ("\t" + topping)
    

users = {
    'npillen' : {
        'first_name': 'nathalie',
        'last_name' : 'pillen',
        'age' : 44
    },
    
    'jkeppens' : {
        'first_name': 'jurgen',
        'last_name' : 'keppens',
        'age' : 46
    }
}

for username, userinfo in users.items():
        print ("\nUsername : " + username)
        full_name = userinfo['first_name'] + " " + userinfo['last_name']
        print (full_name)



        
    



        

    
          


