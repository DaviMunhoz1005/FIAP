def id_valid_hour(hour, minutes):
    return hour <= 24 and minutes <= 59


assert id_valid_hour(12, 30) is True
assert id_valid_hour(12, 30) is True
assert id_valid_hour(0, 0) is True
assert id_valid_hour(23, 59) is True
assert id_valid_hour(24, 0) is True
assert id_valid_hour(12, 60) is False
assert id_valid_hour(25, 60) is False
assert id_valid_hour(25, 12) is False
print("Todos os testes passaram!")
