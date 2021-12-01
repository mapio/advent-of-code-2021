prev = None
cnt = 0
with open('input1.txt') as inf:
  for line in inf:
    n = int(line.strip())
    if prev is not None and n > prev: cnt += 1
    prev = n
print(cnt)