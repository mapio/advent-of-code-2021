with open('input1.txt') as inf:
  nums = list(map(int, inf.readline().strip().split(',')))

costs = []
for x in range(min(nums), max(nums) + 1):
  cost = 0
  for n in nums:
    d = abs(n - x)
    cost += (d * (d + 1)) // 2
  costs.append((cost, x))

print(min(costs)[0])