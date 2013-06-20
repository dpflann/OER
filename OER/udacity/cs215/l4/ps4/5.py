def up_heapify(L, i):
    if i == 0:
        return
    parent_index = parent(i)
    if L[i] < L[parent_index]:
        swap(L, i, parent_index)
        up_heapify(L, parent_index)
    else:
        return
    
def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

def test():
    L = [2, 4, 3, 5, 9, 7, 7]
    L.append(1)
    up_heapify(L, 7)
    assert 1 == L[0]
    assert 2 == L[1]

test()
