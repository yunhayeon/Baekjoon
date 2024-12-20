from collections import deque
import sys
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
q = deque([])
ans = 0

for n in range(N):
  for m in range(M):
    if lst[n][m] == 'I':
      q.append((n, m))
      visited[n][m] = 1

    elif lst[n][m] == 'X':
      visited[n][m] = 1

while q:
  i, j = q.popleft()

  for d in range(4):
    ni = i + di[d]
    nj = j + dj[d]

    if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
      if lst[ni][nj] == 'P':
        ans += 1

      visited[ni][nj] = 1
      q.append((ni, nj))

if ans:
  print(ans)
else:
  print('TT')