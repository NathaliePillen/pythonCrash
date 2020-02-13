user_names = ['beheerder', 'Nathalie', 'Jurgen', 'Annelies', 'Roel']

current_users = ['Raf', 'Sandra', 'Stijn', 'Sofie', 'Bea', 'Gert']

new_users = ['Nathalie', 'Jurgen', 'stijn', 'RAF', 'Mich']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Gebruik een andere username")
    else:
        print("De gebruikersnaam is nog niet in gebruik")     
    


if user_names :
    for user_name in user_names:
        if user_name == 'beheerder':
            print ("Hallo, " + user_name + ", wil je een statusrapport zien? \n")
        else :
            print ("Hallo, " + user_name + ", leuk dat je weer ingelogd bent\n")
else:
    print("We moeten op zoek naar gebruikers!")
    

numbers = list(range(1,10))
for value in numbers:
    if value == 1:
        print(str(value) + "st")
    elif value == 2:
        print(str(value) + "nd")
    else :
        print(str(value) + "th")


              




        



