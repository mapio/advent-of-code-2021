from collections import defaultdict
from sol1 import read
from cube import Cuboid
from tqdm import tqdm, trange

def add(D, s):
  res = {s}
  for r in D: res.update(r - s)
  return res

def remove(D, s):
  res = set()
  for r in D: res.update(r - s)
  return res

data = read('input1.txt')

D = set()
for on, (x1, x2), (y1, y2), (z1, z2) in tqdm(data):
  s = Cuboid(x1, y1, z1, x2 + 1, y2 + 1, z2 + 1)
  D = add(D, s) if on else remove(D, s)

num = 0
for r in D:
  num += r.volume
print(num)