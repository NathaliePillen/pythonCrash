message = input("Tell me something, an I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print('Hello , ' + name)

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your name:"

name = input(prompt)
print('Hello ' + name)

age = input("How old are you?")
age = int(age)
print(age >= 18)


number = input("Enter a number : ")
number = int(number)

if number % 2 == 0:
    print ("The number " + str(number) + " is even")
else:
    print ("The number " + str(nubmer) + " is od")
    



