def valid_plate(plate: str) -> bool:
    if len(plate) != 8 or not plate.__contains__('-'):
        return False
    par1, part2 = plate.split('-')
    if len(par1) != 3 or len(part2) != 4:
        return False
    if not par1.isalpha():
        return False
    if not (part2[0].isdigit() and part2[1].isalpha() and part2[2].isdigit() and part2[3].isdigit()):
        return False
    return True


def digit_or_letter(char: str) -> str:
    return 'letra' if char.isalpha() else 'digito' if char.isdigit() else 'nenhum'


assert digit_or_letter('a') == 'letra'
assert digit_or_letter('z') == 'letra'
assert digit_or_letter('3') == 'digito'
assert digit_or_letter('@') == 'nenhum'
assert valid_plate("ABC-1D23") == True
assert valid_plate("XYZ-9Z99") == True
assert valid_plate("ABCD1D23") == False
assert valid_plate("ABC-DD23") == False
assert valid_plate("ABC-1DD2") == False
assert valid_plate("AB-1D234") == False
assert valid_plate("ABC-1D234") == False
print("Passou todos os testes!")

