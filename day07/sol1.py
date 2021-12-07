with open('input1.txt') as inf:
  nums = list(map(int, inf.readline().strip().split(',')))

print(min(
  [(sum(abs(n-x) for n in nums), x) for x in range(min(nums), max(nums) + 1)]
)[0])