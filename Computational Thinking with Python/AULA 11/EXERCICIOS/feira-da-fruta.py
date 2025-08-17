def price(fruits: list[str]) -> float:
    total = 0.0
    for item in fruits:
        if item == "Banana":
            total += 1.5
        elif item == "Abacate":
            total += 4.99
        elif item == "Tomate":
            total += 3.25

    return total


assert price(['Banana']) != None
assert price(['Banana']) == 1.5
assert price(['Abacate', 'Tomate']) == 8.24
assert price(['Banana', 'Banana']) == 3
assert price([]) == 0
print("todos os testes passaram!")
