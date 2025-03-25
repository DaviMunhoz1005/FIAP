velocity_car = float(input('Qual a velocidade do carro: '))
max_velocity = float(input('Qual a velocidade máxima da rua: '))

if velocity_car <= max_velocity:
    print(f'Não Tomou Multa')
else:
    percentage_ahead = velocity_car / max_velocity

    fine_value = 0
    if percentage_ahead >= 1.5:
        fine_value = 880.41
    elif percentage_ahead > 1.2:
        fine_value = 195.23
    else:
        fine_value = 130.16

    print(f'Tomou Multa no valor de {fine_value}')