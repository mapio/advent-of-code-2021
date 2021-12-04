class Board:
  N = 5
  def __init__(self):
    self.mat = []
    self.marked = []
    self.used = False
  def append(self, row):
    self.mat.append(row)
    self.marked.append([False] * Board.N)
  def __repr__(self):
    return '\n'.join(' '.join([f'{v:2}{"*" if m else " "}' for v, m in zip(vrow, mrow)]) for vrow, mrow in zip(self.mat, self.marked))
  def mark(self, val):
    for vrow, mrow in zip(self.mat, self.marked):
      for c in range(Board.N):
        if vrow[c] == val: mrow[c] = True
  def done(self):
    for row in self.marked:
      if all(row): return True
    for c in range(Board.N):
      if all(self.marked[_][c] for _ in range(Board.N)): return True
  def val(self):
    s = 0
    for vrow, mrow in zip(self.mat, self.marked):
      for v, m in zip(vrow, mrow):
        if not m: s += v
    return s

boards = []
with open('input1.txt') as inf:
  draws = inf.readline()
  inf.readline()
  board = Board()
  for line in inf:
    line = line.strip()
    if not line:
      boards.append(board)
      board = Board()
      continue
    board.append(list(map(int, line.strip().split())))
boards.append(board)

last = None
for val in map(int, draws.strip().split(',')):
  for board in boards:
    board.mark(val)
    if (not board.used) and board.done():
      board.used = True
      last = val * board.val()

print(last)