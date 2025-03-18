year = input('Insira um ano: ')
year = int(year)

actual_year = 2025
is_past = year < actual_year
is_present = year == actual_year
is_future = year > actual_year
is_not_present = is_past or is_future

if is_past:
    print(f'O ano informado está no passado.')
elif is_present:
    print(f'O ano informado é o presente.')
else:
    print(f'O ano informado está no futuro.')