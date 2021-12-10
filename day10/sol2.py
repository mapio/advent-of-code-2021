SCORES = {
 ')': 1,
 ']': 2,
 '}': 3,
 '>': 4
}

TOC = {
 '(': ')',
 '[': ']',
 '{': '}',
 '<': '>'
}

def penality(line):
  stack = []
  for c in line:
    if c in TOC:
      c = TOC[c]
      stack.append(c)
    else:
      p = stack.pop()
      if p != c: return 0
  if stack:
    n = 0
    for c in stack[::-1]:
      n *= 5
      n += SCORES[c]
  return n

s = []
with open('input1.txt') as inf:
  for line in inf:
    p = penality(line.strip())
    if p: s.append(p)
print(sorted(s)[len(s)//2])