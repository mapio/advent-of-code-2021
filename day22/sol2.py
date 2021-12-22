from collections import defaultdict
from sol1 import read
from rect import Rectangle
from tqdm import tqdm, trange

def add(D, s):
  res = {s}
  for r in D: res.update(r - s)
  return res

def remove(D, s):
  res = set()
  for r in D: res.update(r - s)
  return res

z2D = defaultdict(set)

data = read('input1.txt')

for on, (x1, x2), (y1, y2), (z1, z2) in tqdm(data):
  s = Rectangle(x1, y1, x2 + 1, y2 + 1)
  for z in trange(z1, z2 + 1, leave = False):
    z2D[z] = add(z2D[z], s) if on else remove(z2D[z], s)

num = 0
for D in z2D.values():
  for r in D:
    num += r.area
print(num)