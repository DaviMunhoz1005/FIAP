def my_age(birth_year):
    return 2025 - birth_year

birth_year = input('Insira o ano que você nasceu: ')
birth_year = int(birth_year)
age = my_age(birth_year)

print(f'Possui {age} anos, ou {age - 1} anos se ainda não fez aniversário')