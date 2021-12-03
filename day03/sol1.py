from collections import Counter

cts = [Counter() for _ in range(12)]
with open('input1.txt') as inf:
  for line in inf:
    for b, c in zip(line.strip(), cts):
      c.update(b)

x = ''.join(c.most_common(1)[0][0] for c in cts)
y = ''.join(c.most_common(2)[1][0] for c in cts)

print(int(x, 2) * int(y, 2))
