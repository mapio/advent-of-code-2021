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


h, v = FOLDS[0]
dots = set()
if h == 'y':
  for x, y in DOTS:
    if y <= v:
      dots.add((x, y))
    else:
      dots.add((x, 2 * v - y))
else:
  for x, y in DOTS:
    if x <= v:
      dots.add((x, y))
    else:
      dots.add((2 * v - x, y))

print(len(dots))