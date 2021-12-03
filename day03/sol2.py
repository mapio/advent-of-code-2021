from collections import Counter

with open('input1.txt') as inf:
  lst = [_.strip() for _ in inf.readlines()]

def counts(lst, p):
  c = Counter()
  for line in lst: c.update(line[p])
  mc = c.most_common()
  return mc[0][0] if len(mc) == 1 or mc[0][1] > mc[1][1] else '1'

def flt(lst, rev = False):
  p = 0
  while len(lst) > 1:
    b = counts(lst, p)
    if rev: b = '0' if b == '1' else '1'
    lst = [_ for _ in lst if _[p] == b]
    p += 1
  return int(lst[0], 2)

print(flt(lst[:]) * flt(lst[:], True))