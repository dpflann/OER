## Theta(n)

import random
n = 25
rrange = 500
numbers = [ random.randrange(rrange) for i in range(n) ]

## find the max and min, then find the midpoint

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
  set_n = { n for n in L }
  minimum = select_smallest(list(set_n))
  maximum = select_largest(list(set_n))
  midpoint = (1.0 * (maximum + minimum)) / 2
  return midpoint

numbers = [2,2,3,4]
print(sorted(numbers))
print(select_smallest(numbers))
print(select_largest(numbers))
print(minimize_square(numbers))
