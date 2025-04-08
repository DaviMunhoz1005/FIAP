phone_list = ['11987654321', '2187654321', '11912345678', '21987654321']
ddd = 11


def check_start_digits(phone_number, number_to_compare):
    if phone_number.startswith(str(number_to_compare)):
        return True
    else:
        return False


for phone in phone_list:
    if check_start_digits(phone, 11):
        print(f'O telefone {phone} é do DDD {ddd}')
    else:
        print(f'O telefone {phone} não é do DDD {ddd}')
