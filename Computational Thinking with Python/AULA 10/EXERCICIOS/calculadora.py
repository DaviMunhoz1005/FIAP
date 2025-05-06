firstNumber = float(input("First number: "))
secondNumber = float(input("Second number: "))
operation = input("Operation (+, -, *, /): ")


def calculator(firstNumber, secondNumber, operation):
    match operation:
        case "+":
            return f"{firstNumber} + {secondNumber} = {firstNumber + secondNumber}"
        case "-":
            return f"{firstNumber} - {secondNumber} = {firstNumber - secondNumber}"
        case "*":
            return f"{firstNumber} * {secondNumber} = {firstNumber * secondNumber}"
        case "/":
            return f"{firstNumber} / {secondNumber} = {firstNumber / secondNumber}"
        case _:
            return "Operação Inválida"

print(calculator(firstNumber, secondNumber, operation))

assert calculator(6, 3, '+') == f"{6} + {3} = {6 + 3}"
assert calculator(6, 3, '-') == f"{6} - {3} = {6 - 3}"
assert calculator(6, 3, '*') == f"{6} * {3} = {6 * 3}"
assert calculator(6, 3, '/') == f"{6} / {3} = {6 / 3}"
assert calculator(6, 3, 'A') == "Operação Inválida"