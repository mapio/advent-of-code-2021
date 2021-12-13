DOTS = set()
FOLDS = []

with open('input1.txt') as inf:
  for line in inf:
    line = line.strip()
    if not line: break
    x, y = map(int, line.split(','))
    DOTS.add((x, y))
  for line in inf:
    line = line.strip()
    h, v = line.split('=')
    h, v = h[-1], int(v)
    FOLDS.append((h, v))

dots_p = set(DOTS)
for h, v in FOLDS:
  dots = set()
  if h == 'y':
    for x, y in dots_p:
      if y <= v:
        dots.add((x, y))
      else:
        dots.add((x, 2 * v - y))
  else:
    for x, y in dots_p:
      if x <= v:
        dots.add((x, y))
      else:
        dots.add((2 * v - x, y))
  dots_p = dots

mx = max(x for x, _ in dots)
my = max(y for _, y in dots)
for y in range(my + 1):
  for x in range(mx + 1):
    print('#' if (x, y) in dots else '.', end = '')
  print()
