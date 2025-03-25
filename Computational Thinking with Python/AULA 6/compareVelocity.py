velocity_car = input('Qual a velocidade do carro: ')
velocity_car = float(velocity_car)

max_velocity = input('Qual a velocidade máxima da rua: ')
max_velocity = float(max_velocity)

if velocity_car > max_velocity:
    print(f'Tomou Multa')
else:
    print(f'Não Tomou Multa')