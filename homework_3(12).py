# по строкам
def sum_of_digits (number):
     one = int (number [0])
     two = int (number [1])
     three = int (number [2])
     summa = one + two + three
     return summa

 number = input('Введите 3-х значное число:')

 print('Result equals:', sum_of_digits(number))

# без использования строк
number1 = int(input('Введите 3-х значное число:'))
def sum_of_digits (number1):
    a = number1 // 100
    b = (number1 // 10) % 10
    c = number1 % 10
    summa = a + b + c
    return summa


result1 = sum_of_digits(number1)

print('Result equals:', result1)


