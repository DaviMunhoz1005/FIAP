def get_divisors(number):
    divisors = []
    start = 1
    while start <= number:
        if number % start == 0:
            divisors.append(start)
        start = start + 1
    return divisors


print(get_divisors(500))