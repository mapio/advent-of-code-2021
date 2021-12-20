from operator import itemgetter

class Trench:

  @staticmethod
  def from_chars(cmap, cem):
    return Trench(
      list(''.join(cem)),
      ((0, len(cmap[0])), (0, len(cmap))),
      {(r, c) for r, row in enumerate(cmap) for c, v in enumerate(row) if v == '#'},
      True
    )

  def __init__(self, em, bb, on, flag):
    self.em = em
    self.bb = bb
    self.on = on
    self.flag = flag

  def _on(self, i, j):
    return '1' if ((i, j) in self.on) == self.flag else '0'

  def val(self, i, j):
    b = ''.join((
      self._on(i - 1, j - 1),
      self._on(i - 1, j),
      self._on(i - 1, j + 1),
      self._on(i, j - 1),
      self._on(i, j),
      self._on(i, j + 1),
      self._on(i + 1, j - 1),
      self._on(i + 1, j),
      self._on(i + 1, j + 1)
    ))
    return self.em[int(b, 2)]

  def print(self):
    print(self.flag)
    (mx, Mx), (my, My) = self.bb
    for x in range(mx, Mx + 1):
      for y in range(my, My + 1):
        print('#' if ((x, y) in self.on) == self.flag else '.', end = '')
      print()

  def enhance(self):
    res = set()
    b = 10
    (mx, Mx), (my, My) = self.bb
    for x in range(mx - b, Mx + 1 + b):
      for y in range(my - b, My + 1 + b):
        if (self.val(x, y) == '#') != self.flag: res.add((x, y))
    return Trench(self.em, ((mx - 1, Mx + 1), (my - 1, My + 1)), res, not self.flag)

if __name__ == '__main__':

  with open('input1.txt') as inf:
    EM = []
    for line in inf:
      line = line.strip()
      if not line: break
      EM.append(line)
    MAP = []
    for line in inf:
      line = line.strip()
      if not line: break
      MAP.append(line)

  t = Trench.from_chars(MAP, EM)

  for _ in range(50):
    t = t.enhance()

print(len(t.on))