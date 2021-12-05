from collections import Counter

cnt = Counter()
with open('input1.txt') as inf:
  for line in inf:
    f, t = line.strip().split('->')
    (a, b), (c, d) = f.split(','), t.split(',')
    a, b, c, d = map(int, (a, b, c, d))
    if a == c:
      f, t = min(b, d), max(b, d)
      for i in range(f, t + 1): cnt.update(((a, i),))
    elif b == d:
      f, t = min(a, c), max(a, c)
      for i in range(f, t + 1): cnt.update(((i, b),))

n = 0
for p, c in cnt.items():
  if c > 1:
    print(p)
    n += 1
print(n)