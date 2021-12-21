turn = 0
pts = [0, 0]
pos = [5 - 1, 9 - 1]
rnd = list(range(1, 10001))
used = 0

while pts[0] < 1000 and pts[1] < 1000:
  pos[turn] = (pos[turn] + 3 * (used + 2)) % 10
  pts[turn] += 1 + pos[turn]
  turn = 1 - turn
  used += 3

print(used * pts[turn])