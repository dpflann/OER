# Bonus Practice: Subsets


def subsets(l):
    if len(l) == 0:
        return [[]]
    else:
        subs = subsets(l[1:])
        _subs = []
        for s in subs:
            _subs.append([l[0]] + s)  # with
            _subs.append(s)  # without
        return sorted(_subs, key=len)

_s = subsets(['a', 'b', 'c'])
print(_s)


def subsets_2(master, sub):
    if master == []:
        return [sub]
    else:
        elem = master[0]
        remainder = master[1:]
        return sorted(subsets_2(remainder, sub + [elem]) + subsets_2(remainder, sub), key=len)

_s = subsets_2(['a', 'b', 'c'], [])
print(_s)


def test_subsets():
    answer_table = {
        tuple([]): [[]],
        tuple(['a']): [[], ['a']],
        tuple(['a', 'b']): [[], ['a'], ['b'], ['a', 'b']]
    }
    for q, a in answer_table.items():
        assert(subsets(list(q)) == a)
        assert(subsets_2(list(q), []) == a)

test_subsets()

