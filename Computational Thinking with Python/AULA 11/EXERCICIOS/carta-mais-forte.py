def stronger_card(card1: str, card2: str) -> str:
    value_card1 = 0
    value_card2 = 0
    if card1 != 'A':
        value_card1 = int(card1) or 10
    if card2 != 'A':
        value_card2 = int(card2) or 10

    if value_card1 > value_card2 or (card1 == 'A' and value_card2 == 9):
        return 'carta 1'
    elif value_card1 == value_card2:
        return 'iguais'
    return 'carta 2'


assert stronger_card('2', '3') == 'carta 2'
assert stronger_card('9', '9') == 'iguais'
assert stronger_card('7', '8') == 'carta 2'
assert stronger_card('2', '5') == 'carta 2'
assert stronger_card('A', '9') == 'carta 1'
assert stronger_card('A', '2') == 'carta 2'
print('passou todos os testes!')
