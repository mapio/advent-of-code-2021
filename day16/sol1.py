from sys import argv

tobin = lambda hex: ('0000' + bin(int(hex, 16))[2:])[-len(hex) * 4:]

def parse(bits):
  v, k, bits = int(bits[:3], 2), int(bits[3:6], 2), bits[6:]
  if k == 4: # literal
    res = []
    while True:
      blk, bits = bits[:5], bits[5:]
      res.append(blk[1:])
      if blk[0] == '0': break
    return [v, k, int(''.join(res), 2)], bits
  else: # operator
    lk, bits = bits[0], bits[1:]
    if lk == '0': # length
      subl = int(bits[:15], 2)
      rbits, bits = bits[15: 15 + subl], bits[15 + subl:]
      res = []
      while '1' in rbits:
        pkt, rbits = parse(rbits)
        res.append(pkt)
      return [v, k, res], bits
    else: # packet num
      subn, bits = int(bits[:11], 2), bits[11:]
      res = []
      for _ in range(subn):
        pkt, bits = parse(bits)
        res.append(pkt)
      return [v, k, res], bits

def sv(pkt):
  v, k, sub = pkt
  if k == 4:
    return v
  else:
    s = v
    for p in sub:
      s += sv(p)
    return s

if __name__ == '__main__':
  pkt, lo = parse(tobin(argv[1]))
  print(sv(pkt))
