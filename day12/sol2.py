from collections import defaultdict, Counter
from string import ascii_lowercase

small = lambda s: all(c in frozenset(ascii_lowercase) for c in s)

def ok(sol):
  cnt = Counter(n for n in sol if small(n) and n != 'start')
  twice = False
  for c in cnt.values():
    if c > 2: return False
    if c == 2:
      if twice: return False
      twice = True
  return True

G = defaultdict(set)
with open('input1.txt') as inf:
  for line in inf:
    f, t = line.strip().split('-')
    G[f].add(t)
    G[t].add(f)

def bt(sol):
  if not ok(sol): return
  last = sol[-1]
  if last == 'end':
    ALL.add(sol)
    return
  for next in G[last]:
    if next == 'start': continue
    bt(sol + (next,))

ALL = set()
bt(('start',))
print(len(ALL))

