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




@tracer
def permutations(arr):
    if len(arr) == 1:
        return [arr[:]]  # важно вернуть копию!

    output = []

    for _ in range(len(arr)):
        # берём первый элемент
        n = arr.pop(0)

        # перестановки для оставшихся
        perms = permutations(arr)  

        # добавляем n в копию каждой перестановки
        for p in perms:
            output.append(p + [n])

        arr.append(n) 

    return output
