def primes(number):
    listPrimes = []
    for i in range(2, number + 1):
        if isPrime(i):
            listPrimes.append(i)
    return listPrimes



def isPrime(number):
    start = 2
    while start <= number ** 1/2:
        if number % start == 0:
            return False
        start = start + 1
    return True


numberInterval = 100

print(f"List of primes in interval 2 to {numberInterval}: {primes(numberInterval)}")