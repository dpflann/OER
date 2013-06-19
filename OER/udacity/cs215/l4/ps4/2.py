import random

def minimize_absolute(L):
    x = 0
    # your code here
    x = select(L, len(L) / 2)
    return x


def select(L, k):
    if not L:
        return -1
    l = []
    g = []
    e = []
    pivot = L[random.randrange(len(L))]
    for n in L:
        if n < pivot:
            l.append(n)
        elif n > pivot:
            g.append(n)
        else:
            e.append(n)
    if len(l) > k:
        return select(l, k)
    elif len(l) + len(e) >= k:
        return pivot
    elif len(g) > k:
        return select(g, k - len(l) - len(e))

L = [ 1, 2, 3]

print minimize_absolute(L)


