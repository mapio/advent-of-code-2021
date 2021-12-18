from math import floor, sqrt

tx =  281, 311
ty = -74, -54

vx_min = floor((-1 + sqrt(1 + 8 * tx[0])) / 2)
vx_max = tx[1]
vy_min = ty[0]
vy_max = -ty[0]

def traj(vx, vy):
  x, y = 0, 0
  X, Y = [], []
  while True:
    X.append(x)
    Y.append(y)
    if tx[0] <= x <= tx[1] and ty[0] <= y <= ty[1]: return True, X, Y
    if x > tx[1]: return False, X, Y
    if vy < 0 and y < ty[0]: return False, X, Y
    x += vx
    y += vy
    if vx: vx = vx + (-1 if vx > 0 else 1)
    vy -= 1

y_max = 0
cnt = 0
for vx in range(vx_min, vx_max + 1):
  for vy in range(vy_min, vy_max):
    s, x, y = traj(vx, vy)
    if s:
      cnt += 1
      if max(y) > y_max: y_max = max(y)

print(y_max, cnt)