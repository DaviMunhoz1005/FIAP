year = input('Insira um ano: ')

year = int(year)

is_olympics = (year - 2020) % 4 == 0
is_cup = year % 4 == 2

if is_olympics:
    print(f'No ano de {year} terá olimpíadas.')
elif is_cup:
    print(f'No ano de {year} terá copa.')
else:
    print(f'No ano de {year} não terá nada')
