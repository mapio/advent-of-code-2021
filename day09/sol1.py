from itertools import product
import numpy as np

mat = []
with open('input1.txt') as inf:
  for line in inf:
    mat.append(list(map(int, line.strip())))

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

mat = np.array(mat)
r, c = mat.shape
n = 0
for i, j in product(range(r), range(c)):
  if l(mat, i, j):
    n += mat[i, j] + 1

print(n)
