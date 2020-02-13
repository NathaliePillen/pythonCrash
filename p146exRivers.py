rivers = {
    'Egypte' : 'De Nijl',
    'Italië' : 'Arno',
    'België' : 'De Schelde'
}

for country, river in rivers.items():
    print (river + " loopt door " + country)
    print (country)
    print (river)

favorite_languages = {
    'nathalie' : 'Python',
    'jurgen' : 'Javascript',
    'Edward' : 'Ruby',
    'Phil' : 'Python'
    }

persons = ['nathalie', 'Jurgen', 'Mich', 'Raf']

for name in favorite_languages.keys():
    if name.title() in persons or name.lower() in persons:
        print("Hello " + name.title() + " please fill in the form.")    

    