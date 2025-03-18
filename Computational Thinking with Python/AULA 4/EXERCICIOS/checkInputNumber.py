number = input('Insira um número positivo, negativo ou neutro: ')
number = int(number)

is_positive = number > 0
is_negative = number < 0
is_zero = number == 0

if is_positive:
    print(f'O número {number} é positivo.')
elif is_negative:
    print(f'O número {number} é negativo')
else:
    print(f'O número {number} é nulo')