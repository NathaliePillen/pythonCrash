def describe_pet(animal_type, animal_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type)
    print("My  " + animal_type + "'s name is " + animal_name.title())

describe_pet('cat', 'maurice')
describe_pet('dog', 'jean')

def make_shirt(size='L', text='I love Python'):
    print("\nEr wordt een tshirt gemaakt in maat " + size)
    print("met de volgende opdruk:\n" +  text)
    
make_shirt()
make_shirt(text = 'Fake it till you make it', size='M')
    