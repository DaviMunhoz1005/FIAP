number = int(input("Number: "))


def sumOdds(number):
    sum = 0
    for i in range(2, number + 1):
        if i % 2 == 0:
            sum = sum + i
    return sum


print(f"Sum of Odds in this interval is {sumOdds(number)}")

assert sumOdds(10) == 30
assert sumOdds(2) == 2
assert sumOdds(6) == 12
assert sumOdds(7) == 12
