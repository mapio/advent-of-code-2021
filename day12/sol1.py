from collections import defaultdict
from string import ascii_lowercase

small = lambda s: all(c in frozenset(ascii_lowercase) for c in s)

G = defaultdict(set)
with open('input1.txt') as inf:
  for line in inf:
    f, t = line.strip().split('-')
    G[f].add(t)
    G[t].add(f)

def bt(sol):
  last = sol[-1]
  if last == 'end':
    ALL.add(sol)
    return
  for next in G[last]:
    if next == 'start' or (small(next) and next in sol): continue
    bt(sol + (next,))

ALL = set()
bt(('start',))
print(len(ALL))