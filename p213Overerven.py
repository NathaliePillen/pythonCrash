class Car():
    '''Represent a car.'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print('The car has ' + self.odometer_reading + ' miles on it.')
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricalCar(Car):
    '''Represent a car, specific an electrical vehicles.'''
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery." )
        
your_tesla = ElectricalCar('tesla', 'model s', 2016)
print(your_tesla.get_descriptive_name())
your_tesla.describe_battery()



