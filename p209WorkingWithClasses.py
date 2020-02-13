class Car:
    #initialize the attributes in class Car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 1000

    #functie om volledige naamsbeschrijving van de auto weer te geven
    def get_descriptive_name(self):
        full_name_car = str(self.year) + ' '+ self.make + ' ' + self.model
        print(full_name_car + "\nThe car has " + str(self.odometer_reading) + "km")
        
    #functie om de teller te updaten
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print(mileage)
        else:
            print("ERROR")
        
    
    #functio om de teller te verhogen
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        print("The new mileage is " + str(self.odometer_reading))
    
    

my_car = Car('Peugeot', 'Partner', 2015)
my_car.get_descriptive_name()

my_car.odometer_reading = 15000
my_car.get_descriptive_name()

my_newcar = Car('Audi', 'A4', 2019)

my_newcar.update_odometer(2000)
my_newcar.get_descriptive_name()

my_newcar.increment_odometer(1000)

my_newcar.update_odometer(1000)




        