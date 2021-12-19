def split(snailfish):

  pos2node = dict()
  cnt = 0
  split = None
  parent = None
  def add_depth(num, depth = 0):
    nonlocal cnt, split, parent
    l, r = num
    if isinstance(l, list):
      add_depth(l, depth + 1)
    else:
      cnt += 1
      pos2node[cnt] = 'l', num
    if isinstance(r, list):
      add_depth(r, depth + 1)
    else:
      cnt += 1
      pos2node[cnt] = 'r', num
    if parent is None and depth == 3 and (isinstance(l, list) or isinstance(r, list)):
      parent = num
      split = cnt - 1, cnt

  add_depth(snailfish)

  if parent:
    l, r = parent
    if isinstance(l, int):
      ta = parent[1]
      parent[1] = 0
    if isinstance(r, int):
      ta = parent[0]
      parent[0] = 0

    ls, rs = split
    if ls - 1 in pos2node:
      w, ln = pos2node[ls - 1]
      ln[0 if w == 'l' else 1] += ta[0]
    if rs + 1 in pos2node:
      w, rn = pos2node[rs + 1]
      rn[0 if w == 'l' else 1] += ta[1]


num = [[[[[9,8],1],2],3],4]
num = [7,[6,[5,[4,[3,2]]]]]
num = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
num = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
num = [[6,[5,[4,[3,2]]]],1]
print(num)
split(num)
print(num)