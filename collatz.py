
def collatz(input_num):
    while input_num != 1:
        print (input_num, end = ' ')
        if input_num % 2 == 0:
            input_num = input_num // 2
        else:
            input_num = 3 * input_num + 1
    print (1, end='')

while True:
    try:
        input_num = int(input('Enter a positive number: '))
        if input_num <= 0:
            print('please enter a positive integer greater than 0.')
            continue
        break

    except ValueError:
        print ('Invalid input: Please enter a valid integer')
print('Collatz Sequence', end= ' ')
collatz(input_num)
