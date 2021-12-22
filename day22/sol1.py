from itertools import product

def read(path):
  res = []
  with open(path) as inf:
    for line in inf:
      on = True if line.startswith('on') else False
      rx, ry, rz = map(lambda _: tuple(map(int, _.split('..'))), map(lambda _: _.split(',')[0], line.strip().split('=')[1:]))
      res.append((on, rx, ry, rz))
  return res

def adjrange(r):
  f, t = r
  f, t = min(50, max(-50, f)), max(-50, min(50, t))
  if f < t: return range(f, t + 1)
  return []

if __name__ == '__main__':
  board = set()

  for on, rx, ry, rz in read('input1.txt'):
    for x, y, z in product(adjrange(rx), adjrange(ry), adjrange(rz)):
      if on: board.add((x, y, z))
      elif (x, y, z) in board: board.remove((x, y, z))

  print(len(board))