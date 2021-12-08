from itertools import permutations

SEGMENTS = 'abcdefg'
DIGITS = 'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'

PERMS = []
for p in permutations(SEGMENTS):
  t = str.maketrans(SEGMENTS, ''.join(p))
  f = str.maketrans(''.join(p), SEGMENTS)
  PERMS.append((f, frozenset(''.join(sorted(d.translate(t))) for d in DIGITS)))

n = 0
with open('input1.txt') as inf:
  for line in inf:
    l, r = line.strip().split('|')
    d = frozenset(''.join(sorted(_)) for _ in l.split())
    for f, pd in PERMS:
      if pd == d:
        n += int(''.join(map(str, (DIGITS.index(''.join(sorted(o.translate(f)))) for o in r.split()))))
        break
print(n)
