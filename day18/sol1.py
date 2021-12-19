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

num = [[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]], [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]

NUMS = (
  [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
  [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
  [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
  [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
  [7,[5,[[3,8],[1,4]]]],
  [[2,[2,2]],[8,[8,1]]],
  [2,9],
  [1,[[[9,3],9],[[9,0],[0,7]]]],
  [[[5,[7,4]],7],1],
  [[[[4,2],2],6],[8,7]]
)


sum, *NUMS = NUMS

for op in NUMS:
  num = [sum, op]
  while True:
    if explode(num): continue
    if not split(num): break
  sum = num

print(sum)