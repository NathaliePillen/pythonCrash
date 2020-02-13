#exercise 1
properties_0 = {
    'first_name' : 'Nathalie', 
    'last_name' : 'Pillen', 
    'age' : 44, 
    'city' : 'Gent'
    }

properties_1 = {
    'first_name' : 'Jurgen', 
    'last_name' : 'Keppens', 
    'age' : 46, 
    'city' : 'Gent'
    }

properties_2 = {
    'first_name' : 'Roel', 
    'last_name' : 'Jacobs', 
    'age' : 45, 
    'city' : 'Gent'
    }

people = [properties_0, properties_1, properties_2]


for person in people:
    print("Dis zijn de gegevens van volgende klant: ")
    print(person['first_name'])
    print(person['last_name'])
    
    print(person['age'])
    print(person['city'])
    
#exercise 2

animal_1 = {
    'name' : 'maurice',
    'species' : 'cat',
    'owner' : 'nathalie'
}

animal_2 = {
    'name' : 'jean',
    'species' : 'dog',
    'owner' : 'annelies'
}

pets = [animal_1, animal_2]

for animal in pets:
        print (animal['name'] + " is a " + animal['species'] + ". The owner is " + animal['owner'] )
        
#exercise 3

        




   

