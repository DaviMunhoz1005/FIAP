firstNumber = input("Insira o primeiro número: ").replace(",", ".")
secondNumber = input("Insira o segundo número: ").replace(",", ".")

firstNumber = float(firstNumber)
secondNumber = float(secondNumber)

if firstNumber > secondNumber:
    print(f'O primeiro número é o maior com valor {firstNumber}')
elif secondNumber < firstNumber:
    print(f'O segundo número é o maior com valor {secondNumber}')
else:
    print(f'Os números são iguais')