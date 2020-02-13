#we beginnen met een lijst van niet bevestigde gebruikers - de lijst van bevestigde gebruikers is nog leeg
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#zolang de lijst van niet bevestigde gebruikers niet leeg is, is de huidige gebruiker gelijk aan de laatste uit de lijst, we drukken deze af en voegen deze toe aan bevestigde gebruikers de pop-functie verwijdert deze uit de eerste lijst
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print(confirmed_users)
    
#geef alle bevestigde gebruikers weer
print ("\nVolgende gebruikers zijn bevestigd: ")
for confirmed_user in confirmed_users:
    print(confirmed_user)
    

#verwijder een bepaalde waarde uit een lijst
pets = ['dog', 'cat', 'dog', 'fish', 'bird', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)




