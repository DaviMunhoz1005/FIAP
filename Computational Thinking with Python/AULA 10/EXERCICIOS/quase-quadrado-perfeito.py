def almostPerfectSquare(number):
    sqrt = number ** (1 / 2)
    sqrtPlusOne = (number + 1) ** (1 / 2)
    sqrtMinusOne = (number - 1) ** (1 / 2)
    if sqrt.is_integer() or sqrtPlusOne.is_integer() or sqrtMinusOne.is_integer():
        return True
    return False


assert almostPerfectSquare(25) == True
assert almostPerfectSquare(24) == True
assert almostPerfectSquare(26) == True
assert almostPerfectSquare(36) == True
assert almostPerfectSquare(23) == False
assert almostPerfectSquare(16) == True
assert almostPerfectSquare(17) == True
assert almostPerfectSquare(15) == True
assert almostPerfectSquare(14) == False
