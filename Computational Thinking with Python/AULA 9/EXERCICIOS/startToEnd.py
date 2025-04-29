def get_interval_numbers(start, end):
    numbers = []
    while start <= end:
        numbers.append(start)
        start = start + 1
    return numbers


print(get_interval_numbers(1, 10))