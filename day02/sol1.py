pos, depth = 0, 0
with open('input1.txt') as inf:
  for line in inf:
    d, v = line.split()
    v = int(v)
    if d == 'forward':
      pos += v
    elif d == 'up':
      depth -= v
    else:
      depth += v
print(pos * depth)
