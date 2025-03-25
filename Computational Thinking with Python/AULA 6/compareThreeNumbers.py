firstNumber = input('Qual o primeiro número: ')
secondNumber = input('Qual o segundo número: ')
thirdNumber = input('Qual o terceiro número: ')

firstNumber = float(firstNumber)
secondNumber = float(secondNumber)
thirdNumber = float(thirdNumber)

if firstNumber > secondNumber and firstNumber > thirdNumber:
    if secondNumber > thirdNumber:
        print(f'Maior valor é {firstNumber} Menor é {thirdNumber}')
    else:
        print(f'Maior valor é {firstNumber} Menor é {secondNumber}')
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    if firstNumber > thirdNumber:
        print(f'Maior valor é {secondNumber} Menor é {thirdNumber}')
    else:
        print(f'Maior valor é {secondNumber} Menor é {firstNumber}')
else:
    if secondNumber > firstNumber:
        print(f'Maior valor é {thirdNumber} Menor é {firstNumber}')
    else:
        print(f'Maior valor é {thirdNumber} Menor é {secondNumber}')
