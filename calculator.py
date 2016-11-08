import os
os.system('clear')

def calculator(a , b , operation = '+', output_format = 'float'):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return 'You entered wrong values'
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        result = a / b

    if output_format == 'float':
        return result
    elif output_format == 'int':
        return round(result) # rounds the result to int
    else:
        return 'Wrong format of output'

print(calculator(input('first number: '),input('second number: '),
input('operation: '),input('output format: ')))
