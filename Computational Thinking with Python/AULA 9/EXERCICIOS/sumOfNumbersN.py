def get_interval_sum(end):
    start = 1
    sum = 0
    while start <= end:
        sum = sum + start
        start = start + 1
    return sum


print(get_interval_sum(10))