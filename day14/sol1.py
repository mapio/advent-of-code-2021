from collections import Counter

MAP = dict()
with open('input1.txt') as inf:
  START = inf.readline().strip()
  inf.readline()
  for line in inf:
    f, t = map(lambda _: _.strip(), line.split('->'))
    MAP[f] = t

polymer = START[:]
for _ in range(10):
  res = [polymer[0]]
  last = False
  for i in range(len(polymer) - 1):
    f = polymer[i:i + 2]
    if f in MAP:
      res.extend((MAP[f], f[1]))
    else:
      res.extend(f)
  polymer = ''.join(res)

v = sorted(Counter(polymer).values())
print(v[-1] - v[0])
