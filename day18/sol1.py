def explode(snailfish):

  pos2node = dict()
  cnt = 0
  explode = None
  parent = None
  def add_depth(num, depth = 0):
    nonlocal cnt, explode, parent
    l, r = num
    le = None
    if isinstance(l, list):
      le = cnt
      add_depth(l, depth + 1)
    else:
      cnt += 1
      pos2node[cnt] = 'l', num
    if isinstance(r, list):
      if le is None: le = cnt
      add_depth(r, depth + 1)
    else:
      cnt += 1
      pos2node[cnt] = 'r', num
    if parent is None and depth == 3 and (isinstance(l, list) or isinstance(r, list)):
      parent = num
      explode = le + 1, le + 2

  add_depth(snailfish)

  if parent is None: return False
  l, r = parent
  if isinstance(l, list):
    ta = parent[0]
    parent[0] = 0
  elif isinstance(r, list):
    ta = parent[1]
    parent[1] = 0

  ls, rs = explode
  if ls - 1 in pos2node:
    w, ln = pos2node[ls - 1]
    ln[0 if w == 'l' else 1] += ta[0]
  if rs + 1 in pos2node:
    w, rn = pos2node[rs + 1]
    rn[0 if w == 'l' else 1] += ta[1]

  return True

def split(snailfish):
  split = False

  def _split(num):
    nonlocal split
    if split or isinstance(num, int): return
    l, r = num
    if isinstance(l, list):
      _split(l)
    elif not split and l >= 10:
      split = True
      num[0] = [l // 2, l - (l // 2)]
    if isinstance(r, list):
      _split(r)
    elif not split and r >= 10:
      split = True
      num[1] = [r // 2, r - (r // 2)]

  _split(snailfish)
  return split

def sum(a, b):
  sum = [a, b]
  while True:
    if explode(sum): continue
    if not split(sum): break
  return sum

def mag(snailfish):
  if isinstance(snailfish, int):
    return snailfish
  else:
    l, r = snailfish
    return 3 * mag(l) + 2 * mag(r)

if __name__ == '__main__':
  res = None
  with open('input1.txt') as inf:
    for line in inf:
      lst = eval(line)
      if res is None:
        res = lst
      else:
        res = sum(res, lst)
  print(mag(res))