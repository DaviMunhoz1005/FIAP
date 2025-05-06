def isMap(list):
    if len(list) == 0:
        return False
    for i in list:
        if i != '.' and i != 'o':
            return False
    return True


assert isMap(['.', '.', '.','o']) == True
assert isMap(['o', 'o', 'o','.']) == True
assert isMap(['.', 'o', '.']) == True
assert isMap([]) == False
assert isMap(['.', 'x', '.']) == False