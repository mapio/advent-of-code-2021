from collections import defaultdict
from functools import total_ordering
from heapq import *

with open('input1.txt') as inf: G = [list(map(int, line.strip())) for line in inf]

@total_ordering
class Node:
  def __init__(self, coord):
    self.coord = coord
  def __eq__(self, other):
    return self.coord == other.coord
  def __hash__(self):
      return hash(self.coord)
  def __lt__(self, other):
    return DIST[self] < DIST[other]
  def __repr__(self):
    return f'Node({self.coord})'

def neigh(u):
  for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
    yield Node((u.coord[0] + d[0], u.coord[1] + d[1]))

def enter(v):
  v = v.coord
  cond = v[0] < 0 or v[0] >= len(G) or v[1] < 0 or v[1] >= len(G)
  return float('inf') if cond else G[v[0]][v[1]]

SRC = Node((0, 0))
DST = Node((len(G) - 1, len(G) - 1))
DIST = defaultdict(lambda : float('inf'))
DIST[SRC] = 0
Q = [SRC]

while Q:
  u = heappop(Q)
  for v in neigh(u):
    alt = DIST[u] + enter(v)
    if alt < DIST[v]:
      DIST[v] = alt
      if v in Q:
        heapify(Q)
      else:
        heappush(Q, v)

print(DIST[DST])