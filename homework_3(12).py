def sum_of_digits (number):
    one = int(number [0])
    two = int(number[1])
    three = int(number [2])
    summa = one + two + three
    return summa

number = input('Введите 3-х значное число:')

print('Result equials:', sum_of_digits(number))
