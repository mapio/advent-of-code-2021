from z3 import BitVec, BitVecVal, If, Optimize

z3var = lambda _: BitVec(_, 64)
z3val = lambda _: BitVecVal(_, 64)

def z3fresh():
  z3fresh.n += 1
  return z3var(f'v_{z3fresh.n}')
z3fresh.n = 0

DIGITS = [z3var(f'd_{i}') for i in range(14)]
NUMBER = sum(d * (10 ** e) for e, d in enumerate(DIGITS[::-1]))
ZERO, ONE = z3val(0), z3val(1)
REGISTERS = {v: ZERO for v in 'xyzw'}

solver = Optimize()

digit_input = iter(DIGITS)
with open('input1.txt') as inf:
    for i, line in enumerate(inf):
        inst, *args = line.strip().split()
        if inst == 'inp':
            REGISTERS[args[0]] = next(digit_input)
        else:
          a, b = args
          b = REGISTERS[b] if b in REGISTERS else int(b)
          c = z3fresh()
          if inst == 'add':
              solver.add(c == REGISTERS[a] + b)
          elif inst == 'mul':
              solver.add(c == REGISTERS[a] * b)
          elif inst == 'mod':
              solver.add(REGISTERS[a] >= 0)
              solver.add(b > 0)
              solver.add(c == REGISTERS[a] % b)
          elif inst == 'div':
              solver.add(b != 0)
              solver.add(c == REGISTERS[a] / b)
          elif inst == 'eql':
              solver.add(c == If(REGISTERS[a] == b, ONE, ZERO))
          REGISTERS[a] = c

solver.add(REGISTERS['z'] == 0)
for d in DIGITS: solver.add(1 <= d, d <= 9)

for obj in (solver.maximize, solver.minimize):
    solver.push()
    obj(NUMBER)
    solver.check()
    m = solver.model()
    print(''.join([str(m[d]) for d in DIGITS]))
    solver.pop()