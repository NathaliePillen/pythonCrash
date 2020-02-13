properties = {'first_name' : 'Nathalie', 'last_name' : 'Pillen', 'age' : 44, 'city' : 'Gent'}

print (properties['first_name'])
print (properties['last_name'])
print (properties['age'])
print (properties['city'])

lucky_numbers = {
    'nathalie' : 8,
    'Jurgen' : 14,
    'Sandra' : 66,
    'Raf' : 28
    }

print (lucky_numbers)

print ('Nathalie her lucky number is ' + 
       str(lucky_numbers['nathalie']))

print ('Jurgen his lucky number is ' + 
       str(lucky_numbers['Jurgen']))

# lussen door key-value pairs
for name, number in lucky_numbers.items():
    print ("Lucky number of " + 
           name.title() + 
           " is " + str(number) + "!\n")

#lussen door keys
for name in lucky_numbers.keys():
    print (name.title())
    

    
    




