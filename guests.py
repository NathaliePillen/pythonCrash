guests = ['Ben', 'Els', 'Stijn', 'Sofie', 'Juan', 'Sophie']
print(guests)

message = "Dag " + guests[0] + ", Graag nodig ik je uit voor een etentje!"
print (message)

not_present = guests.pop(4)
print ("\n" + not_present + " kan niet aanwezig zijn.")

print (guests)
guests.insert(4,'Pierre')
print (guests)

#sort method
guests.sort()
print (guests)

guests.sort(reverse=True)
print (guests)

#sorted method (enkel weergave volgorde van lijst blijft behouden)
print(sorted(guests))
print (guests)

#omgekeerde volgorde
guests.reverse()
print(guests)

#aantal items in de lijst weergeven
print(len(guests))






