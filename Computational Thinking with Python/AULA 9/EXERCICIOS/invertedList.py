def invert_list(list):
    inverse_list = []
    i = len(list) - 1
    while i >= 0:
        inverse_list.append(list[i])
        i = i - 1
    return inverse_list

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(invert_list(list))