bicycles = ["gazelle", "oxford", "trek", "koga", "brompton"]
print (bicycles)
print ("\n\t" + bicycles[0].title())

#laatste uit de lijst met hoofdletter
print ("\n\t" + bicycles[-1].title())

#voorlaatste uit de lijst met hoofdletter
print ("\n\t" + bicycles[-2].title())

message = "\n\tMy first bicycle was a " + bicycles[0].title() + "."
print(message)

names = ['nathalie', 'Jurgen', 'Annelies', 'Roel', 'Sandra', 'Raf']
print (names[0])
print (names[1])
print (names[2])

message = "Beste " + names[0] + "! \nIk wens jou een prettig weekend!"
print (message)

# item in lijst veranderen
names[4]='Riet'
print(names)

#item in lijst achteraan toevoegen
names.append('Erik')
print(names)

#item in lijst op positie toevoegen
names.insert(3, 'Mich')
print (names)

#item verwijderen
del names[3]
print (names)

names.remove('nathalie')
print(names)

#pop-methode laatste item ophalen en nadien nog weergeven
popped_name = names.pop()
print ("\n" + popped_name)

popped_name = names.pop(1)
print ("\n" + popped_name)

car="Renault"
print("Is car == 'Renault'? I predict True.")
print(car.lower()=="renault")


print("\nIs car == 'audi'? I predict False.")
print(car=="audi")

print(names)
print(names=='nathalie')

print ('nathalie' in names)


if 'nathalie' not in names:
    names.append('nathalie')
    print (names)
    

    






