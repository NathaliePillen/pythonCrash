user_0 = {
    'username' : 'npillen',
    'name' : 'Nathalie',
    'last_name' : 'Pillen'
    }

for key, value in user_0.items():
    print ('\nKey : ' + key)
    print ('Value : ' + value)
    
favorite_languages = {
    'nathalie' : 'Python',
    'jurgen' : 'Javascript',
    'Edward' : 'Ruby',
    'Phil' : 'Python'
    }

#key value
for name, language in favorite_languages.items():
    print(name.title() + 
        "'s favorite language is: " +
        language.title())
    
#only key's
for name in favorite_languages.keys():
    print(name)
    
for name in favorite_languages:
    print(name)
    

friends = ['Sandra', 'Raf', 'Annelies', 'Roel', 'nathalie']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ', I see your favorite language is ' + language.title())
     
    
for languages in set(favorite_languages.values()):
    print (languages)
    
    
    
    