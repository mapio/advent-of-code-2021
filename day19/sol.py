from itertools import permutations, product
import numpy as np

def rotmat():
  for x, y, z in permutations([0, 1, 2]):
    for sx, sy, sz in product([-1, 1], repeat=3):
      R = np.zeros((3, 3))
      R[0, x] = sx
      R[1, y] = sy
      R[2, z] = sz
      if np.linalg.det(R) == 1: yield R

def read(path):
  scanners = []
  with open(path) as inf:
    scanner = []
    for line in inf:
      line = line.strip()
      if not line: continue
      if '--- scanner' in line:
        if scanner: scanners.append(np.array(scanner))
        scanner = []
      else:
        scanner.append(eval(line))
  if scanner: scanners.append(np.array(scanner))
  return scanners

def as_set(arr):
  return set(tuple(r) for r in arr)

def tra_rot(t, s):
  for s_row in s:
    st = as_set(s - s_row)
    for m in Rs:
      r = (t @ m).astype(int)
      for r_row in r:
        i = st & as_set(r - r_row)
        if len(i) >= 12: return s_row - r_row, m
  return None, None

def transf(frm, tra, rot):
  return (tra + frm @ rot).astype(int)

def intersect(s, t):
  return np.array(list(as_set(s) & as_set(t)))

def union(s, t):
  return np.array(list(as_set(s) | as_set(t)))

def invert(tra, rot):
  rot = np.linalg.inv(rot)
  tra = - tra.T @ rot
  return tra, rot

def compose(t, s, tra_ts, rot_ts, bt):
  def _bt(i):
    print(f'{t} -> {s}')
    return bt(transf(i, tra_ts, rot_ts))
  return _bt

def tid(i):
  print('id')
  return i

def visit(s, bt):
  for t in set(range(len(SCANNERS))) - seen:
    tra_ts, rot_ts = tra_rot(SCANNERS[t], SCANNERS[s])
    if tra_ts is None: continue
    btc = compose(t, s, tra_ts, rot_ts, bt)
    i = btc(SCANNERS[t])
    print(f'PROCESSING {t} -> {s}')
    found.append(i)
    pos.append(btc([0,0,0]))
    seen.add(t)
    visit(t, compose(t, s, tra_ts, rot_ts, bt))

Rs = list(rotmat())
SCANNERS = read('input1.txt')

seen = set([0])
found = [SCANNERS[0]]
pos = [np.array([0, 0, 0])]
visit(0, tid)

print('==== RESULTS')

res = set()
for bs in found:
  res |= as_set(bs)
print('Part 1:', len(res))

maxd = 0
for b in pos:
  for c in pos:
    d = np.abs(np.array(b) - np.array(c)).sum()
    if d > maxd: maxd = d
print('Part 2:', maxd)