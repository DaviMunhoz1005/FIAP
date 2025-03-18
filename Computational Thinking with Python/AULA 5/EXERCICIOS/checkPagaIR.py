salary = input('Insira os dígitos do seu salário: ').replace(',', '.')

salary = float(salary)

if salary <= 2212:
    print(f'O salário no valor de R${salary:.2f} não paga imposto de renda (IR)')
else:
    print(f'O salário no valor de R${salary:.2f} paga imposto de renda (IR)')