def get_numbers_one_to_one_hundred():
    numbers = []
    number_to_add = 1
    while number_to_add <= 100:
        numbers.append(number_to_add)
        number_to_add = number_to_add + 1
    return numbers


print(get_numbers_one_to_one_hundred())