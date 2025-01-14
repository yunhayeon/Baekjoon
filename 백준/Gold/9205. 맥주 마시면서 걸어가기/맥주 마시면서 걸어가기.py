from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):

  storeCnt = int(input())
  now = deque([tuple(map(int, input().split()))])
  store = []
  visitedStore = [0 for _ in range(storeCnt)]

  for _ in range(storeCnt):
    store.append(tuple(map(int, input().split())))

  end = list(map(int, input().split()))
  ans = 'sad'

  while now:
    i, j = now.popleft()
    
    if abs(end[0] - i) + abs(end[1] - j) <= 1000:
      ans = 'happy'
      break

    for s in range(storeCnt):
      if not visitedStore[s] and abs(store[s][0] - i) + abs(store[s][1] - j) <= 1000:
        now.append(store[s])
        visitedStore[s] = 1

  print(ans)