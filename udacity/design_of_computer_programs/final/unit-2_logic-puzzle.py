"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop. -->
    if wendesday is laptop
2. The programmer is not Wilkes. -->
    if wilkes is not programmer
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. -->
   if wilkes is programmer and hamming is droid or wilkes is droid and hamming is programmer
4. The writer is not Minsky. -->
    if minksy is not writer
5. Neither Knuth nor the person who bought the tablet is the manager. -->
    if knuth is not manager
    if tablet is not manager
    if knuth is not tablet
6. Knuth arrived the day after Simon. -->
    if knuth - simon is 1
7. The person who arrived on Thursday is not the designer. -->
    if thursday is not designer
8. The person who arrived on Friday didn't buy the tablet. -->
    if friday is not tablet
9. The designer didn't buy the droid. -->
    if designer is not droid
10. Knuth arrived the day after the manager. -->
    if knuth - manager is 1
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer. -->
    if laptop is monday and wilkes is writer or laptop is writer and wilkes is monday
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday. -->
    if iphone is tuesday or tablet is tuesday

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)

Names: ['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']
Jobs:  ['programmer', 'writer', 'manager', 'designer', ]
Items: ['laptop', 'droid', 'tablet', 'iphone' ]
Arrival: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


"""
import itertools

def in_order(**unordered_dict):
    return sorted(unordered_dict, key=lambda value: unordered_dict[value])

def logic_puzzle():
    week = monday, tuesday, wednesday, thursday, friday = [1, 2, 3, 4, 5]
    day_orderings = list(itertools.permutations(week))
    return next(in_order(Hamming=hamming, Knuth=knuth, Minsky=minsky, Simon=simon, Wilkes=wilkes)
        for (hamming, knuth, minsky, simon, wilkes) in day_orderings
        if knuth - simon is 1
        for (programmer, writer, manager, designer, OTHER_JOB) in day_orderings
        if minsky is not writer
        and knuth - manager is 1
        and thursday is not designer
        and wilkes is not programmer
        for (droid, iphone, laptop, tablet, OTHER_ITEM) in day_orderings
        if designer is not droid
        and tablet is not manager
        and knuth is not manager
        and (wilkes is programmer and hamming is droid or wilkes is droid and hamming is programmer)
        and (laptop is monday and wilkes is writer or laptop is writer and wilkes is monday)
        and wednesday is laptop
        and friday is not tablet
        and (iphone is tuesday or tablet is tuesday)
    )
