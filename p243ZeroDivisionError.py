print("Give me two numbers, and i'll devide them\n")
print("Enter 'q' to quit")

while True:
    first_number = input("\nPlease give me a number: ")
    if first_number == 'q':
        break
    second_number = input("\nPlease give me a second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't divide by 0")
    else:
        print (answer)
    
    
        