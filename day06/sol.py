cnts = [0] * 9
cnts = [0] * 9
with open('input1.txt') as inf:
  for n in list(map(int, inf.readline().strip().split(','))):
    cnts[n] += 1

for i in range(256):
  c0, *cnts = cnts + [0]
  cnts[6] += c0
  cnts[8] = c0

print(sum(cnts))
