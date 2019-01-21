def compact(iterable_object):
    iterable_object = iter(iterable_object)
    last_value = iterable_object
    result = []
    while True:
        try:
            next_value = next(iterable_object)
        except StopIteration:
            break
        if next_value == last_value:
            continue
        else:
            last_value = next_value
            result.append(next_value)
    return result

# bonus_2
def compact2(iterable_object):
    iterable_object = iter(iterable_object)
    last_value = compact
    while True:
        try:
            next_value = next(iterable_object)
        except StopIteration:
            break
        if next_value == last_value:
            continue
        else:
            last_value = next_value
            yield next_value


