with open('input1.txt') as inf: nums = list(map(int, inf.readline().strip().split(',')))

cnts = [0] * 9
for n in nums:
  cnts[n] += 1

def step(cnts):
  res = cnts[1:] + [0]
  if cnts[0] > 0:
    res[6] += cnts[0]
    res[8] = cnts[0]
  return res

for i in range(256):
  cnts = step(cnts)

print(sum(cnts))
