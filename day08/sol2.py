from itertools import permutations

SEGMENTS = 'abcdefg'
DIGITS = 'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'

PERMS = []
TRANS = []
for p in permutations(SEGMENTS):
  t = str.maketrans(SEGMENTS, ''.join(p))
  PERMS.append(frozenset(''.join(sorted(d.translate(t))) for d in DIGITS))
  TRANS.append(str.maketrans(''.join(p), SEGMENTS))

n = 0
with open('input1.txt') as inf:
  for line in inf:
    l, r = line.strip().split('|')
    d = frozenset(''.join(sorted(i)) for i in l.split())
    f = TRANS[PERMS.index(d)]
    n += int(''.join(map(str, (DIGITS.index(''.join(sorted(o.translate(f)))) for o in r.split()))))
print(n)
