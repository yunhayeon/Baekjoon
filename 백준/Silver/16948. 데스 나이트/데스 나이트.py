from collections import deque
import sys
input = sys.stdin.readline

di = [-2, -2, 0, 0, 2, 2]
dj = [-1, 1, -2, 2, -1, 1]

N = int(input())
si, sj, ei, ej = map(int, input().split())

q = deque([])
visited = [[0 for _ in range(N)] for _ in range(N)]
find = False
ans = 0

if (si, sj) != (ei, ej):
  visited[si][sj] = 1
  q.append((si, sj))
else:
  find = True

while q:
  lq = len(q)
  ans += 1

  for _ in range(lq):
    i, j = q.popleft()

    for d in range(6):
      ni, nj = i + di[d], j + dj[d]

      if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
        if (ni, nj) == (ei, ej):
          find = True
          break

        visited[ni][nj] = 1
        q.append((ni, nj))

  if find:
    break


if find:
  print(ans)
else:
  print(-1)