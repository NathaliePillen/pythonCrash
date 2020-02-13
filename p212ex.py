class Restaurant:
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("\nThe restaurant " + self.restaurant_name + " is " + self.restaurant_type)
        
    def open_restaurant(self):
        print(self.restaurant_name + " is open")
    
    def print_number_served(self, number):
        self.number_served = number
        print("The number of people that you have served " + self.number_served)
        
        

restaurant_1 = Restaurant('June', 'Italien')

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

print("You are welcome at restaurant " + restaurant_1.restaurant_name)

restaurant_2 = Restaurant('April', 'French')
restaurant_3 = Restaurant('September', 'Portuguese')

restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

print("You are welcome at restaurant " + restaurant_2.restaurant_name)

restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()

print("You are welcome at restaurant " + restaurant_3.restaurant_name)

restaurant = Restaurant ('Jane', 'French')






