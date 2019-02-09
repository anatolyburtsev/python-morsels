def tail(seq, n):
    if n <= 0:
        return []
    values = list()
    for val in seq:
        if len(values) >= n:
            values.pop(0)
        values.append(val)
    return values

print(tail((n**2 for n in range(0)), 2))

