## Theta(n)

import random
n = 25
rrange = 500
numbers = [ random.randrange(rrange) for i in range(n) ]

# select the smallest element in L
def select_smallest(L):
    if not L:
        return -1
    if len(L) == 1:
      return L[0]
    l = []
    e = []
    pivot = L[random.randrange(len(L))]
    for n in L:
        if n < pivot:
            l.append(n)
        elif n == pivot:
            e.append(n)
    if len(l) > 0:
      return select_smallest(l)
    elif len(e) > 0:
      return e[0]

# select the largest element in L
def select_largest(L):
    if not L:
        return -1
    if len(L) == 1:
      return L[0]
    g = []
    e = []
    pivot = L[random.randrange(len(L))]
    for n in L:
        if n > pivot:
            g.append(n)
        elif n == pivot:
            e.append(n)
    if len(g) > 0:
      return select_largest(g)
    elif len(e) > 0:
      return e[0]


def minimize_square(L):
  # mean is the solution
  mean = (1.0 * sum(L)) / (len(L))
  return mean

