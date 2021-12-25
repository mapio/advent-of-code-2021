MAP = []
with open('input1.txt') as inf:
  for line in inf:
    MAP.append(list(line.strip()))
R, C = len(MAP), len(MAP[0])

def p(m):
  print('\n'.join(''.join(r) for r in m))

def step(now):
  moved = False
  then = [['.' for j in range(C)] for i in range(R)]
  for i in range(R):
    for j in range(C):
      if now[i][j] == '>':
        r = (j + 1) % C
        if now[i][r] == '.':
          then[i][r] = '>'
          moved = True
        else:
          then[i][j] = '>'
  for i in range(R):
    for j in range(C):
      if now[i][j] == 'v':
        b = (i + 1) % R
        if (now[b][j] != 'v' and then[b][j] == '.'):
          then[b][j] = 'v'
          moved = True
        else:
          then[i][j] = 'v'
  return moved, then

n = 1
now = MAP
while True:
  m, then = step(now)
  if m == False: break
  n += 1
  now = then

print(n)
