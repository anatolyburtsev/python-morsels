def get_earliest(*args):
    dates = list(args)
    f = lambda i: lambda x: x.split("/")[i]
    dates = sorted(dates, key=f(1))
    dates = sorted(dates, key=f(0))
    dates = sorted(dates, key=f(2))

    return dates[0]