from collections import deque
import sys
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

R, C = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
ans = [0, 0]

for r in range(R):
  for c in range(C):
    if not visited[r][c]:
      visited[r][c] = 1
      q = deque([(r, c)])
      o, v = 0, 0

      while q:
        i, j = q.popleft()

        if lst[i][j] == 'v':
          v += 1
        elif lst[i][j] == 'o':
          o += 1

        for d in range(4):
          ni, nj = i + di[d], j + dj[d]

          if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj]:
            if lst[ni][nj] != '#':
              q.append((ni, nj))
              visited[ni][nj] = 1
            else:
              visited[ni][nj] = 2

      if o > v:
        ans[0] += o
      else:
        ans[1] += v

print(*ans)