#woordenboek - 
alien_0 = {'color':'green','points':5}

print (alien_0['color'])

print (alien_0['points'])

print (alien_0)

alien_0['x-position'] = 0
alien_0['y-position'] = 25

print (alien_0)

del alien_0['color']
print (alien_0)



#begin met een leeg woordenboek - waarden toevoegen
alien_1={}

alien_1['color'] = 'red'
alien_1['points'] = 10

print(alien_1)

#waarden aanpassen

alien_1['color'] = 'yellow'
print (alien_1)

alien_3 ={'position-x': 0, 'position-y': 25, 'speed':'medium'}
print("original x-position: "+ str(alien_3['position-x']))

#move alien_3 to th right
#determine how far to move the alien based on its current speed
if alien_3['speed'] == 'slow':
    x_increment = 1
if alien_3['speed'] == 'medium':
    x_increment = 2
if alien_3['speed'] == 'fast':
    x_increment = 3
    
# the new position is the old postion plus the increment
alien_3['position-x'] = alien_3['position-x'] + x_increment
print("new x-position: " + str(alien_3['position-x']))

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'C',
    'edward' : 'ruby',
    'phil' : 'python'
    }

print ("The favorite language of Sarah is " + 
    favorite_languages['sarah'].title())


