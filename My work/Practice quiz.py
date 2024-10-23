
# SOME PRACTICE QUESTIONS


# Using a function and variables enterd from the keybard, write a progra that allows the user to input a number.
 # If the input is an even number, returns the input divded by two plus 1
# If the input is an odd number, returns a squre of the input.

def even_or_odd_number ():
    number = int(input('Enter the number: \n'))
    if number %2 == 0:
        result = number/2+1
        print(f"{result}")
    else:
        result = number**2
        print(f"{result}")
even_or_odd_number()

# Even this below is correct.

def even_and_odd_numbers():
    number = int(input("Enter the numebr: "))
    if number %2 == 0:
        result = number/2 + 1
        print(f"Number: Even:\n Result: {result:.0f}")
    else:
        #Odd number
        result = number**2
        print(f"Number: Odd:\n Result:{result:.0f}") 

even_and_odd_numbers()



