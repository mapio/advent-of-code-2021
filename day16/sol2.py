from sys import argv

from sol1 import tobin, parse

def val(pkt):
  v, k, sub = pkt
  if k == 4:
    return sub
  elif k == 0:
    return sum(val(s) for s in sub)
  elif k == 1:
    p = 1
    for s in sub:
      p *= val(s)
    return p
  elif k == 2:
    return min(val(s) for s in sub)
  elif k == 3:
    return max(val(s) for s in sub)
  elif k == 5:
    l, r = sub
    return 1 * (val(l) > val(r))
  elif k == 6:
    l, r = sub
    return 1 * (val(l) < val(r))
  elif k == 7:
    l, r = sub
    return 1 * (val(l) == val(r))

pkt, lo = parse(tobin(argv[1]))
print(val(pkt))
