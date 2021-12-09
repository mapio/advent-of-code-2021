from itertools import product
import numpy as np

mat = []
with open('input1.txt') as inf:
  for line in inf:
    mat.append(list(map(int, line.strip())))
mat = np.array(mat)

def m(mat, i, j):
  r, c = mat.shape
  if i < 0 or i >= r: return float('inf')
  if j < 0 or j >= c: return float('inf')
  return mat[i, j]

def l(mat, i, j):
  c = m(mat, i, j)
  return all((
    c < m(mat, i - 1, j),
    c < m(mat, i + 1, j),
    c < m(mat, i, j - 1),
    c < m(mat, i, j + 1)
  ))

def b(mat, i, j):
  basin = {(i, j)}
  while True:
    s = set(basin)
    for i, j in basin:
      if m(mat, i - 1, j) < 9: s.add((i - 1, j))
      if m(mat, i + 1, j) < 9: s.add((i + 1, j))
      if m(mat, i, j - 1) < 9: s.add((i, j - 1))
      if m(mat, i, j + 1) < 9: s.add((i, j + 1))
    if s == basin: break
    basin = s
  return s

r, c = mat.shape
print(np.prod(sorted(
  len(b(mat, i , j)) for i, j in product(range(r), range(c)) if l(mat, i, j)
)[-3:]))
