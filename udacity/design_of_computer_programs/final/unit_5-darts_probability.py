# Unit 5: Probability in the game of Darts

"""
In the game of darts, players throw darts at a board to score points.
The circular board has a 'bulls-eye' in the center and 20 slices
called sections, numbered 1 to 20, radiating out from the bulls-eye.
The board is also divided into concentric rings.  The bulls-eye has
two rings: an outer 'single' ring and an inner 'double' ring.  Each
section is divided into 4 rings: starting at the center we have a
thick single ring, a thin triple ring, another thick single ring, and
a thin double ring.  A ring/section combination is called a 'target';
they have names like 'S20', 'D20' and 'T20' for single, double, and
triple 20, respectively; these score 20, 40, and 60 points. The
bulls-eyes are named 'SB' and 'DB', worth 25 and 50 points
respectively. Illustration (png image): http://goo.gl/i7XJ9

There are several variants of darts play; in the game called '501',
each player throws three darts per turn, adding up points until they
total exactly 501. However, the final dart must be in a double ring.

Your first task is to write the function double_out(total), which will
output a list of 1 to 3 darts that add up to total, with the
restriction that the final dart is a double. See test_darts() for
examples. Return None if there is no list that achieves the total.

Often there are several ways to achieve a total.  You must return a
shortest possible list, but you have your choice of which one. For
example, for total=100, you can choose ['T20', 'D20'] or ['DB', 'DB']
but you cannot choose ['T20', 'D10', 'D10'].
"""

def test_darts():
    "Test the double_out function."
    assert double_out(170) == ['T20', 'T20', 'DB']
    assert double_out(171) == None
    assert double_out(100) in (['T20', 'D20'], ['DB', 'DB'])

"""
My strategy: I decided to choose the result that has the highest valued
target(s) first, e.g. always take T20 on the first dart if we can achieve
a solution that way.  If not, try T19 first, and so on. At first I thought
I would need three passes: first try to solve with one dart, then with two,
then with three.  But I realized that if we include 0 as a possible dart
value, and always try the 0 first, then we get the effect of having three
passes, but we only have to code one pass.  So I created ordered_points as
a list of all possible scores that a single dart can achieve, with 0 first,
and then descending: [0, 60, 57, ..., 1].  I iterate dart1 and dart2 over
that; then dart3 must be whatever is left over to add up to total.  If
dart3 is a valid element of points, then we have a solution.  But the
solution, is a list of numbers, like [0, 60, 40]; we need to transform that
into a list of target names, like ['T20', 'D20'], we do that by defining name(d)
to get the name of a target that scores d.  When there are several choices,
we must choose a double for the last dart, but for the others I prefer the
easiest targets first: 'S' is easiest, then 'T', then 'D'.
"""


def double_out(total):
    """Return a shortest possible list of targets that add to total,
    where the length <= 3 and the final element is a double.
    If there is no solution, return None."""

    # obtain all outcomes
    total_outcomes = set([25, 50])  # include 0 and bulls-eye
    doubles = set([50])
    for i in range(1, 21):
        total_outcomes |= {i, i * 2, i * 3}
        doubles |= {i * 2}
    total_outcomes = [0] + sorted(total_outcomes, reverse=True)
    # create acceptable groups that sum to the total
    groups = []
    darts_1_and_2 = [(i, j, i + j) for i in total_outcomes for j in total_outcomes]
    for combo in darts_1_and_2:
        d_1, d_2, _1_and_2 = combo
        d_3 = total - _1_and_2
        # filter those that do not end on a double
        if d_3 in doubles:
            groups.append((d_1, d_2, d_3))
    # convert the list to alphanumeric representation
    names = [rename(g) for g in groups]
    # select the shortest list
    option = min(names, key=len) if names else None
    return option


def rename(g):
    """Rename a group of darts from numbers to strings.

    60 --> T20 for triple 20.
    """

    return [name(d, i) for i, d in enumerate(g, start=1) if d != 0]


def name(n, i):
    """Rename a number to a string. Select the 'easiest' target is there are many options.

    60 --> T2 for triple 20
    S > T > D
    """

    names = {0: ['OFF'], 25: ['SB'], 50: ['DB']}
    for _ in range(1, 21):
        s, d, t = _, _ * 2, _ * 3
        _s = str(_)
        if s not in names:
            names[s] = ['S' + _s]
        else:
            names[s] += ['S' + _s]
        if d not in names:
            names[d] = ['D' + _s]
        else:
            names[d] += ['D' + _s]
        if t not in names:
            names[t] = ['T' + _s]
        else:
            names[t] += ['T' + _s]
    options = names[n]
    if n == 0:
        return options[0]
    if i == 3:
        # select a double
        option = [o for o in options if 'D' in o]
    else:
        # select the easiest
        option = [o for o in options if 'S' in o]
        if not option:
            option = [o for o in options if 'T' in o]
        if not option:
            option = [o for o in options if 'D' in o]
    return option[0]

### TEST double_out(n)
test_darts()

"""
It is easy enough to say "170 points? Easy! Just hit T20, T20, DB."
But, at least for me, it is much harder to actually execute the plan
and hit each target.  In this second half of the question, we
investigate what happens if the dart-thrower is not 100% accurate.

We will use a wrong (but still useful) model of inaccuracy. A player
has a single number from 0 to 1 that characterizes his/her miss rate.
If miss=0.0, that means the player hits the target every time.
But if miss is, say, 0.1, then the player misses the section s/he
is aiming at 10% of the time, and also (independently) misses the thin
double or triple ring 10% of the time. Where do the misses go?
Here's the model:

First, for ring accuracy.  If you aim for the triple ring, all the
misses go to a single ring (some to the inner one, some to the outer
one, but the model doesn't distinguish between these). If you aim for
the double ring (at the edge of the board), half the misses (e.g. 0.05
if miss=0.1) go to the single ring, and half off the board. (We will
agree to call the off-the-board 'target' by the name 'OFF'.) If you
aim for a thick single ring, it is about 5 times thicker than the thin
rings, so your miss ratio is reduced to 1/5th, and of these, half go to
the double ring and half to the triple.  So with miss=0.1, 0.01 will go
to each of the double and triple ring.  Finally, for the bulls-eyes. If
you aim for the single bull, 1/4 of your misses go to the double bull and
3/4 to the single ring.  If you aim for the double bull, it is tiny, so
your miss rate is tripled; of that, 2/3 goes to the single ring and 1/3
to the single bull ring.

Now, for section accuracy.  Half your miss rate goes one section clockwise
and half one section counter-clockwise from your target. The clockwise
order of sections is:

    20 1 18 4 13 6 10 15 2 17 3 19 7 16 8 11 14 9 12 5

If you aim for the bull (single or double) and miss on rings, then the
section you end up on is equally possible among all 20 sections.  But
independent of that you can also miss on sections; again such a miss
is equally likely to go to any section and should be recorded as being
in the single ring.

You will need to build a model for these probabilities, and define the
function outcome(target, miss), which takes a target (like 'T20') and
a miss ration (like 0.1) and returns a dict of {target: probability}
pairs indicating the possible outcomes.  You will also define
best_target(miss) which, for a given miss ratio, returns the target
with the highest expected score.

If you are very ambitious, you can try to find the optimal strategy for
accuracy-limited darts: given a state defined by your total score
needed and the number of darts remaining in your 3-dart turn, return
the target that minimizes the expected number of total 3-dart turns
(not the number of darts) required to reach the total.  This is harder
than Pig for several reasons: there are many outcomes, so the search space
is large; also, it is always possible to miss a double, and thus there is
no guarantee that the game will end in a finite number of moves.
"""
from collections import defaultdict


def outcome(target, miss):
    sections = "20 1 18 4 13 6 10 15 2 17 3 19 7 16 8 11 14 9 12 5".split()
    results = defaultdict(float)
    for (ring, ringP) in ring_candidates(target, miss):
        for (sect, sectP) in section_candidates(target, miss):
            p = ringP * sectP
            if ring == 'S' and sect.endswith('B'):
                for s in sections:
                    if p > 0.:
                        results[Target(ring, s)] += (p) / 20.
            else:
                if p > 0.:
                    results[Target(ring, sect)] += (ringP * sectP)
    return dict(results)


def section_candidates(target, miss):
    sections = "20 1 18 4 13 6 10 15 2 17 3 19 7 16 8 11 14 9 12 5".split()
    hit = 1.0 - miss
    if target in ('SB', 'DB'):
        misses = [(s, miss/20.) for s in sections]
    else:
        i = sections.index(target[1:])
        misses = [(sections[i-1], miss/2.), (sections[(i+1) % 20], miss/2.)]
    return [(target[1:], hit)] + misses


def ring_candidates(target, miss):
    hit = 1.0 - miss
    r = target[0]  # letter
    if target == 'DB':
        miss = min(3*miss, 1.)
        hit = 1.0 - miss
        return [('DB', hit), ('SB', miss/3.), ('S', 2./3.*miss)]
    elif target == 'SB':
        return [('SB', hit), ('DB', miss/4.), ('S', 3./4.*miss)]
    elif r == 'S':
        return [(r, 1.0 - miss/5.), ('D', miss/10.), ('T', miss/10.)]
    elif r == 'D':
        return [(r, hit), ('S', miss/2.), ('OFF', miss/2.)]
    elif r == 'T':
        return [(r, hit), ('S', miss)]


def Target(ring, section):
    if ring == 'OFF':
        return 'OFF'
    elif ring in ('SB', 'DB'):
        return ring if (section == 'B') else ('S' + section)
    else:
        return ring + section

def best_target(miss):
    "Return the target that maximizes the expected score."
    sections = "20 1 18 4 13 6 10 15 2 17 3 19 7 16 8 11 14 9 12 5".split()
    targets = set(r+s for r in 'SDT' for s in sections) | set(['SB', 'DB'])
    return max(targets, key=lambda t: expected_value(t, miss))


def expected_value(target, miss):
    return sum(value(t) * p for (t, p) in outcome(target, miss).items())


def value(target):
    if target == 'OFF':
        return 0
    multiples = {
        'S': 1,
        'D': 2,
        'T': 3
    }
    _value = target[1:]
    if _value == 'B':
        _value = 25
    else:
        _value = int(_value)
    return multiples[target[0]] * _value


def same_outcome(dict1, dict2):
    "Two states are the same if all corresponding sets of locs are the same."
    return all(abs(dict1.get(key, 0) - dict2.get(key, 0)) <= 0.0001
               for key in set(dict1) | set(dict2))


def test_darts2():
    assert same_outcome(outcome('T20', 0.0), {'T20': 1.0})
    assert same_outcome(outcome('T20', 0.1),
                        {'T20': 0.81, 'S1': 0.005, 'T5': 0.045,
                         'S5': 0.005, 'T1': 0.045, 'S20': 0.09})
    assert (same_outcome(
            outcome('SB', 0.2),
            {'S9': 0.016, 'S8': 0.016, 'S3': 0.016, 'S2': 0.016, 'S1': 0.016,
             'DB': 0.04, 'S6': 0.016, 'S5': 0.016, 'S4': 0.016, 'S20': 0.016,
             'S19': 0.016, 'S18': 0.016, 'S13': 0.016, 'S12': 0.016, 'S11': 0.016,
             'S10': 0.016, 'S17': 0.016, 'S16': 0.016, 'S15': 0.016, 'S14': 0.016,
             'S7': 0.016, 'SB': 0.64}))
    assert best_target(0.0) == 'T20'
    assert best_target(0.1) == 'T20'
    assert best_target(0.4) == 'T19'

test_darts2()


def dismantle(target):
    letters, numbers = [], []
    for c in target:
        if c.isdecimal():
            numbers.append(c)
        elif c.isalpha():
            letters.append(c)
    return ''.join(letters), int(''.join(numbers))


def outcome_2(target, miss):
    """Return a probability distribution of [(target, probability)] pairs.
    """

    if miss == 0.0:
        return {target: miss}
    sections = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]
    probabilities = {}
    if target == 'SB' or target == 'DB':
        # deal with this last
        return probabilities
    # determine sections that can receive a dart given the miss probability
    # based upon section, determined by value
    ring, section = dismantle(target)
    target_index = sections.index(section)
    clockwise_miss = sections[target_index + 1]
    counterclockwise_miss = sections[target_index - 1]
    # determine ring misses and probabilities per section
    target_section_probability = 1 - miss
    miss_section_probability = miss / 2.0
    sections = [(section, target_section_probability), (clockwise_miss, miss_section_probability), (counterclockwise_miss, miss_section_probability)]
    for s, p in sections:
        for _probability, _target in ring_candidates(ring, s, p, miss):
            probabilities[_target] = _probability
    return probabilities


def ring_candidates_2(ring, section, section_probability, miss):
    results = []
    if ring == 'T':
        # hit T or S
        hit_T = (section_probability * (1 - miss), 'T' + str(section))
        hit_S = (section_probability * (miss), 'S' + str(section))
        results.extend([hit_T, hit_S])
    elif ring == 'D':
        # hit S or OFF or D
        hit_D = (section_probability * (1 - miss), 'D' + str(section))
        hit_S = (section_probability * (miss / 2.0), 'S' + str(section))
        hit_OFF = (section_probability * (miss / 2.0), 'OFF')
        results.extend([hit_D, hit_S, hit_OFF])
    elif ring == 'S':
        # hit S or T or D
        # adjust miss
        new_miss = miss / 5.0
        hit_S = (section_probability * (1 - new_miss), 'S' + str(section))
        hit_T = (section_probability * (new_miss / 2.0), 'T' + str(section))
        hit_D = (section_probability * (new_miss / 2.0), 'D' + str(section))
        results.extend([hit_S, hit_T, hit_D])
    return results