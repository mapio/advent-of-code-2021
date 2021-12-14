from collections import defaultdict

MAP = dict()
with open('input1.txt') as inf:
  START = inf.readline().strip()
  inf.readline()
  for line in inf:
    f, t = map(lambda _: _.strip(), line.split('->'))
    MAP[f] = t

PAIRS = defaultdict(int)
for i in range(len(START) - 1):
  PAIRS[START[i:i + 2]] += 1

prev = dict(PAIRS)
for _ in range(40):
  pairs = defaultdict(int)
  for k, v in prev.items():
    if k in MAP:
      pairs[k[0] + MAP[k]] += prev[k]
      pairs[MAP[k] + k[1]] += prev[k]
  prev = dict(pairs)

cnt = defaultdict(int)
cnt[START[0]] = 1
cnt[START[-1]] = 1
for k, v in pairs.items():
  cnt[k[0]] += v
  cnt[k[1]] += v

v = sorted(cnt.values())
print((v[-1] - v[0])//2)