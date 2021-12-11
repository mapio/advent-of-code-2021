import numpy as np

res = []
with open('input1.txt') as inf:
  for line in inf:
    res.append(list(map(int, line.strip())))
M = np.array(res)
R, C = M.shape

def inc1(M, i, j):
  if i < 0 or i >= R or j < 0 or j >= C: return
  M[i, j] += 1

def inc(M, i, j):
  inc1(M, i - 1, j - 1)
  inc1(M, i - 1, j)
  inc1(M, i - 1, j + 1)
  inc1(M, i, j - 1)
  inc1(M, i, j + 1)
  inc1(M, i + 1, j - 1)
  inc1(M, i + 1, j)
  inc1(M, i + 1, j + 1)

def step(M):
  M = M + 1
  f = np.zeros_like(M)
  while True:
    s = f.sum()
    for i in range(R):
      for j in range(C):
        if M[i, j] > 9 and f[i, j] == 0:
          f[i, j] = 1
          inc(M, i, j)
    if f.sum() == s: break
  M[f == 1] = 0
  return f.sum(), M

n = 0
for i in range(100):
  s, M = step(M)
  n += s
print(n)
