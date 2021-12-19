from copy import deepcopy
from itertools import product

from sol1 import mag, sum

with open('input1.txt') as inf: NUMS = [eval(line) for line in inf]

max = 0
for a, b in product(NUMS, NUMS):
  v = mag(sum(deepcopy(a), deepcopy(b)))
  if v > max: max = v
print(max)