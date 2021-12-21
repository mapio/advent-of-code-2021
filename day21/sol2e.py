from itertools import product
from collections import defaultdict, namedtuple

dice2cnt = defaultdict(int)
for i, j, k in product(range(1, 4), range(1, 4), range(1, 4)):
  dice2cnt[i + j + k] += 1
dice2cnt = dict(dice2cnt)

Universe = namedtuple('Universe', 'pos, pts')

U = {Universe((4, 8), (0, 0)): 1}

turn = 0
wins = [0, 0]

while U:
  Up = defaultdict(int)
  for u, uc in U.items():
    for d, dc in dice2cnt.items():
      npos = list(u.pos)
      npts = list(u.pts)
      npos[turn] = (npos[turn] + d) % 10
      npts[turn] += npos[turn] + 1
      Up[Universe(tuple(npos), tuple(npts))] += uc * dc
  U = defaultdict()
  for u, uc in Up.items():
    if u.pts[turn] >= 21:
      wins[turn] += uc
    else:
      U[u] = uc
  turn = 1 - turn

print(max(wins))