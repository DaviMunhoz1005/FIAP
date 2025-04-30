def isPrime(number):
    start = 2
    while start <= number ** 1/2:
        if number % start == 0:
            return False
        start = start + 1
    return True


print(isPrime(2))
print(isPrime(3))
print(isPrime(53))
print(isPrime(5))
print(isPrime(97))

