
def collatz(input_num):
    while input_num != 1:
        print (input_num, end = ' ')
        if input_num % 2 == 0:
            input_num = input_num // 2
        else:
            input_num = 3 * input_num + 1
    print (1, end='')

input_num = int(input('Enter a positive number: '))
print('Collatz Sequence', end= ' ')
collatz(input_num)
