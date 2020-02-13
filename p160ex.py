car_input = input("Welke auto had u graag gehad : ")
print("We gaan voor u op zoek naar een " + car_input)

persons = input("Met hoeveel mensen had u willen reserveren?")
persons = int(persons)

if persons > 8 :
    print("Eventjes wachten, wij maken een tafel klaar.")
else:
    print("u kan meteen aan tafel")

number = input("Please enter a number ")
number = int(number)

if number % 10 == 0:
    print("Het cijfer " + str(number) + " is een veelvoud van 10")
else :
    print("Het nummer " + str(number) + " is geen veelvoud van 10")


    
     