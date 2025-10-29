import functools


def tracer(fn):
    lvl = 0   

    def inside(*args):
        nonlocal lvl
        
        print("__" * lvl + f": {fn.__name__}{args}")

        lvl += 1
        res = fn(*args)
        lvl -= 1

        print("__" * lvl + f": {fn.__name__}{args} = {res}")

        return res

    return inside

