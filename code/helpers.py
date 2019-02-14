def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)

    wrapped.calls = 0
    return wrapped


def tracked(f):
    def wrapped(*args, **kwargs):
        wrapped.grids.append(str(args[1]))
        return f(*args, **kwargs)

    wrapped.grids = []
    return wrapped





