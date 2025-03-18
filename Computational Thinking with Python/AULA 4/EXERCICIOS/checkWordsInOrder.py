def compare_characters(first, second):
    for c1, c2 in zip(first.lower(), second.lower()):
        if c1 != c2:
            return c1 <= c2
    return len(first) <= len(second)


first_word = input('Insira a primeira palavra: ')
second_word = input('Insira a segunda palavra: ')

if compare_characters(first_word, second_word):
    print(f'A primeira palavra e a segunda estão em ordem alfabética correta.')
else:
    print(f'A primeira palavra e a segunda não estão em ordem alfabética correta.')
