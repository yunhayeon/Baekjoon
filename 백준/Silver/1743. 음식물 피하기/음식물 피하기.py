from collections import deque
import sys
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M, K = map(int, input().split())
lst = set()
visited = set()
ans = 0

for _ in range(K):
  r, c = map(int, input().split())
  lst.add((r, c))

for r, c in lst:
  if (r, c) not in visited:
    cnt = 0
    q = deque([(r, c)])
    visited.add((r, c))

    while q:
      cnt += 1
      i, j = q.popleft()

      for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if (ni, nj) in lst and (ni, nj) not in visited:
          q.append((ni, nj))
          visited.add((ni, nj))

    if ans < cnt:
      ans = cnt

print(ans)