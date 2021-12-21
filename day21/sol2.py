from itertools import product
from collections import defaultdict
from typing import NewType

sum2cnt = defaultdict(int)
for i, j, k in product(range(1, 4), range(1, 4), range(1, 4)): sum2cnt[i + j + k] += 1
sum2cnt = dict(sum2cnt)
sum2cnt = {1:2, 2:1}
print(sum2cnt)


pos2cnt = [[0] * 10, [0] * 10]
pos2cnt[0][3] = 1
pos2cnt[1][7] = 1

pts2cnt = [defaultdict(int), defaultdict(int)]
pts2cnt[0][0] = 1
pts2cnt[1][0] = 1

wins = [0, 0]
turn = 0
while len(pts2cnt[0]) > 0 and len(pts2cnt[0]):

    print('turn', turn)

    next_pos2cnt = [0] * 10
    for s, cs in sum2cnt.items():
      for p in range(10):
        next_pos2cnt[(p + s) % 10] += pos2cnt[turn][p] * cs
    pos2cnt[turn] = next_pos2cnt

    print('pos2cnt', pos2cnt[turn])

    next_pts2cnt = defaultdict(int)
    for pts, cnt in pts2cnt[turn].items():
      for pos in range(10):
        if pos2cnt[turn][pos]:
          next_pts2cnt[pts + pos + 1] += cnt * pos2cnt[turn][pos]
    pts2cnt[turn] = next_pts2cnt

    todel = []
    for p in pts2cnt[turn]:
      if p >= 21:
        wins[turn] += pts2cnt[turn][p]
        todel.append(p)
    for p in todel: del pts2cnt[turn][p]

    print('wins', wins[turn], 'pts2cnt', dict(pts2cnt[turn]))

    turn = 1 - turn

# sum2cnt2 = defaultdict(int)
# for s0, c0 in sum2cnt.items():
#   for s1, c1 in sum2cnt.items():
#     sum2cnt2[s0 + s1] += c0 * c1

# print(sum2cnt2)