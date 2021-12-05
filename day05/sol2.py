from collections import Counter

cnt = Counter()
with open('input1.txt') as inf:
  for line in inf:
    f, t = line.strip().split('->')
    (a, b), (c, d) = f.split(','), t.split(',')
    a, b, c, d = map(int, (a, b, c, d))
    if a == c:
      s = 1 if b < d else -1
      for i in range(b, d + s, s): cnt.update(((a, i),))
    elif b == d:
      s = 1 if a < c else -1
      for i in range(a, c + s, s): cnt.update(((i, b),))
    else:
      s = 1 if a < c else -1
      t = 1 if b < d else -1
      for i in range(a, c + s, s):
        cnt.update(((i, b),))
        b += t

n = 0
for p, c in cnt.items():
  if c > 1: n += 1
print(n)