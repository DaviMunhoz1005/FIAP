import re


def is_valid_phone(digits):
    return 7 < digits < 12


def how_many_digits(phone_number):
    phone_number = re.sub(r'[-() ]', '', phone_number)
    return len(phone_number)


phone_number = input('Digite o telefone: ')
digits = how_many_digits(phone_number)

if is_valid_phone(digits):
    print("O número de telefone é válido!")
else:
    print("Número de telefone inválido! Deve ter entre 8 e 11 dígitos.")
