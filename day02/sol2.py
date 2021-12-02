pos, depth, aim = 0, 0, 0
with open('input1.txt') as inf:
  for line in inf:
    d, v = line.split()
    v = int(v)
    if d == 'forward':
      pos += v
      depth += aim * v
    elif d == 'up':
      aim -= v
    else:
      aim += v
print(pos * depth)
