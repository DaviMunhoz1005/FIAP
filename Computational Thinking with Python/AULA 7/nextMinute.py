def add_one_minute(time):
    hours = int(time)
    minutes = round((time - hours) * 1000)

    minutes += 1
    while minutes >= 60:
        hours += 1
        minutes -= 60

    return f'{hours}:{minutes:02d}'

time = input('Digite o tempo (hh,mm): ').replace(',', '.')
time = float(time)

print(add_one_minute(time))
