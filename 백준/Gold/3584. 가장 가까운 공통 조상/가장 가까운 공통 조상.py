from collections import deque
import sys
input = sys.stdin.readline

road1, road2 = [], []

def findParents(s):
  global road1, road2

  road = [s]
  q = deque([s])

  while q:
    now = q.popleft()

    if tree[now]:
      road.append(tree[now])
      q.append(tree[now])

  if road1:
    road2 = road
  else:
    road1 = road


T = int(input())
for _ in range(T):
  N = int(input())
  tree = [0 for _ in range(N + 1)]
  for _ in range(N - 1):
    A, B = map(int, input().split())
    tree[B] = A
  N1, N2 = map(int, input().split())
  
  findParents(N1)
  findParents(N2)

  for r in road1:
    if r in road2:
      print(r)
      road1, road2 = [], []
      break

  