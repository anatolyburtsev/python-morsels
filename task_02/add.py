def add(*args):
    result_list = []
    for l in zip2(*args):
        mini_list = []
        for i in zip2(*l):
            mini_list.append(sum(i))
        result_list.append(mini_list)
    return result_list


def zip2(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        to_fail = False
        finish_reached = False
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                finish_reached = True
            else:
                to_fail = True
            result.append(elem)
        if finish_reached and to_fail:
            raise ValueError()
        if finish_reached:
            return
        yield tuple(result)

