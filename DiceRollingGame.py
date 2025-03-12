#Dice rolling game
#a question 'roll the dice?' needs to pop up accepting only two options Y or N
#any other answer should throw an error message
#Y should give two random numbers
#N should thank the user
import random

while True:
    choice = input ('Roll dice? (Y/N): ').lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print ('Thanks for playing!')
        break
    else:
        print ('Invalid choice')