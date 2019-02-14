from operator import itemgetter
from collections import defaultdict
from itertools import groupby


def group_by(iterable_obj, key_func=lambda x: x):
    d = defaultdict(list)
    for o in iterable_obj:
        d[key_func(o)].append(o)
    return dict(d.iteritems())


def group_by2(iterable_obj, key_func=lambda x: x):
    iterable_obj = sorted(iterable_obj, key=key_func)
    g = groupby(iterable_obj, key_func)
    result = dict()
    for k, v in g:
        result[k] = list(v)
    return result


print(group_by2(["one", "one", "two", "one"]))

