from itertools import product
from collections import defaultdict, namedtuple

sum2cnt = defaultdict(int)
for i, j, k in product(range(1, 4), range(1, 4), range(1, 4)):
  sum2cnt[i + j + k] += 1
sum2cnt = dict(sum2cnt)
sum2cnt = {3:1, 2:1}
print(sum2cnt)

Universe = namedtuple('Universe', 'pos, pts')

U = {Universe((3, 7), (0, 0)): 1}

turn = 0
wins = [0, 0]

while U:
  Up = defaultdict(int)
  for u, uc in U.items():
    for d, dc in sum2cnt.items():
      npos = list(u.pos)
      npts = list(u.pts)
      npos[turn] = (npos[turn] + d) % 9
      npts[turn] += npos[turn] + 1
      Up[Universe(tuple(npos), tuple(npts))] += uc * dc
  U = defaultdict()
  for u, uc in Up.items():
    if u.pts[turn] >= 21:
      wins[turn] += uc
    else:
      U[u] = uc
  for u, uc in U.items(): print(uc, (u.pos[0], u.pts[0]), (u.pos[1], u.pts[1]))
  turn = 1 - turn
  print(wins)

print(max(wins) / 444356092776315)