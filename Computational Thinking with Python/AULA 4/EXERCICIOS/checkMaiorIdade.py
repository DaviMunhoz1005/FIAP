birth_year = input('Insira seu ano de nascimento: ')
birth_year = int(birth_year)

actual_year = 2025

person_age = actual_year - birth_year
of_legal_age = person_age >= 18

if of_legal_age:
    print(f'Você possui {person_age} anos, logo é maior de idade.')
else:
    print(f'Você possui {person_age} anos, logo é menor de idade.')