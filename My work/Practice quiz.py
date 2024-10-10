
# SOME PRACTICE QUESTIONS


# Using a function nad variables enterd fro the keybard, write a progra that allows the user to input a number.
 # If the input is an even number, returns the input divded by two plus 1
# If the input is an off number, returns a squre of the input.

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



