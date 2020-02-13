dogs = ['labrador', 'retriever', 'spaniel', 'beagle']
for dog in dogs:
    message = "Mijn favoriete hondenras is " + dog.title()
    print(message)
    print("Ik zou graag een " + dog.title() + " trainen. \n")
    
pizzas = ['margarita', 'caesar', 'fungi', '4 seizoenen']
for pizza in pizzas:
    print ("Ik ben gek op pizza " + pizza + "\n")
    
print("Who doesn't love pizza")

players = ['nathalie', 'Jurgen', 'Annelies', 'Roel', 'Sandra', 'Raf']
print (players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players of my team")
for player in players[0:3]:
    print (player)
    
    
print("The last three players of my team")
for player in players[-3:]:
    print (player)

friend_pizzas = pizzas[:]
friend_pizzas.append('4 kazen')
print(pizzas)
print(friend_pizzas)

for pizza in pizzas:
    print(pizza)
    
for pizza in friend_pizzas:
    print(pizza)
    
dimensions = (20,100)
print('original dimensions:')
for dimension in dimensions:
    print(dimension)
    
dimensions = (50,500)
print('changed dimensions:')
for dimension in dimensions:
    print(dimension)
    

gerechten = ('tomaat garnaal', 'steak', 'zalm', 'hamburger', 'mosselen')
for gerecht in gerechten:
    print (gerecht)
    


gerechten = ('spaghetti', 'steak', 'zalm', 'hamburger', 'croque')
print ("\nNieuwe menu:")
for gerecht in gerechten:
    print (gerecht)
    




    