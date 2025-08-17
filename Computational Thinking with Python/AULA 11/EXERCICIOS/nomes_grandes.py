def bigger_name(names: list[str]) -> list[str]:
    bigger_names = []
    for name in names:
        if len(name) > 10:
            bigger_names.append(name)

    return bigger_names


assert bigger_name(["Joao", "Constantinos"]) == ["Constantinos"]
assert bigger_name([]) == []
assert bigger_name(["Ana", "Pedro", "Alexandrino"]) == ["Alexandrino"]
assert bigger_name(["Alexandrino", "Bernardinos", "Carlos"]) == ["Alexandrino", "Bernardinos"]
assert bigger_name(["Maria", "Jose", "Gabrielinos"]) == ["Gabrielinos"]
print("Todos os testes passam!")
