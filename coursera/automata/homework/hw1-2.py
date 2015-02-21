## Homework 1 - Problem 2

automaton = { "A" : { "0" : "B" , "1" : "C" }, "B" : { "1" : "D" }, "C" : { "0" : "D" }, "D" : { "0" : "A", "1" : "B" } }

def delta(w, state):
  if w == '':
    return ''
  for i in w:
    if i in automaton[state].keys():
      state = automaton[state][i]
    else:
      return ''
  return state

import itertools as it
def wordsAcceptedForLength(length):
  strings = list(it.product("01", repeat=length))
  acceptedStrings = map(lambda t: ''.join(t), [ string for string in strings if delta(string, "A") == "D" ])
  return len(acceptedStrings), acceptedStrings

def acceptedStringsPerLength(limit, showWords=False):
  for l in range(limit + 1):
    length, words = wordsAcceptedForLength(l)
    print "N(%d) = %d" % (l, length)
    if showWords:
      print "words accepted: ", words

def test():
  assert delta("", "A") == ''
  assert delta("0", "A") == "B"
  assert delta("01", "A") == "D"
  assert delta("0111001", "A") == "D"
  assert delta("11", "C") == ''
  length, words = wordsAcceptedForLength(0)
  assert length == 0
  assert words == []
  length, words = wordsAcceptedForLength(1)
  assert length == 0
  assert words == []
  length, words = wordsAcceptedForLength(2)
  assert length == 2
  print "tests pass"
