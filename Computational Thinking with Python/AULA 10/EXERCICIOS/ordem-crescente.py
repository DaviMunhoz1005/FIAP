def isGrowing(firstNumber, secondNumber, thirdNumber):
    if firstNumber < secondNumber < thirdNumber:
        return True
    return False


running = True
while running != 0:
    firstNumber = float(input("First number: "))
    secondNumber = float(input("Second number: "))
    thirdNumber = float(input("Third number: "))

    if isGrowing(firstNumber, secondNumber, thirdNumber):
        print(f"The numbers is growing")
    else:
        print(f"The numbers is not growing")

    running = int(input("Try Again? (1 or 0)"))

assert isGrowing(1, 2, 3) == True
assert isGrowing(3, 2, 1) == False
assert isGrowing(2, 2, 3) == False
