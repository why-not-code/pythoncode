#Let code guess a number
#As user guesses the number, the code gives feedback like 'too high' or 'too low'

import random

number = random.randint(1,100)

#try except block to catch error
while True:
    try:
        choice = int(input('Make a guess between 1 and 100: '))

        if choice < number:
            print ("too low")
        elif choice > number:
            print ("too high")
        else:
            print("correct guess; congrats")
            break
    except ValueError:
        print ('please enter a valid number')
