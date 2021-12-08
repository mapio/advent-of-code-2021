LENS = frozenset({2, 3, 4, 7})

n = 0
with open('input1.txt') as inf:
  for line in inf:
    _, o = line.strip().split('|')
    for c in o.split():
      if len(c) in LENS: n += 1
print(n)
