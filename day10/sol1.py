SCORES = {
 ')': 3,
 ']': 57,
 '}': 1197,
 '>': 25137
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
      if p != c:
        return SCORES[c]
  return 0

n = 0
with open('input1.txt') as inf:
  for line in inf:
    n += penality(line.strip())
print(n)