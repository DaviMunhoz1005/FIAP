def get_interval_numbers(end):
    numbers = []
    start_number = 1
    while start_number <= end:
        if start_number % 2 == 1:
            numbers.append(start_number)
        start_number = start_number + 1
    return numbers


print(get_interval_numbers(10))
