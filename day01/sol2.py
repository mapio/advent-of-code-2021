import numpy as np

v = np.loadtxt('input1.txt')
#v = np.array([1,2,3,4,5,6,7,8])
s = v[:-2] + v[1:-1] + v[2:]
print(sum(s[1:] > s[:-1]))