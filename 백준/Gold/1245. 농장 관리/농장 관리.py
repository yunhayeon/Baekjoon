from collections import deque
import sys
input = sys.stdin.readline

di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
ans = 0

for r in range(N):
  for c in range(M):
    if not visited[r][c]:
      visited[r][c] = 1
      now = deque([(r, c)])
      top = deque([(r, c)])
      isSmall = True

      while top:
        i, j = top.popleft()

        for d in range(8):
          ni, nj = i + di[d], j + dj[d]

          if 0 <= ni < N and 0 <= nj < M and lst[i][j] == lst[ni][nj] and (ni, nj) not in now:
            visited[ni][nj] = 1
            now.append((ni, nj))
            top.append((ni, nj))
      
      if lst[r][c] > 0:
        while now:
          i, j = now.popleft()

          for d in range(8):
            ni, nj = i + di[d], j + dj[d]

            if 0 <= ni < N and 0 <= nj < M:
              if lst[i][j] < lst[ni][nj]:
                isSmall = False
              else:
                visited[ni][nj] = 1

        if isSmall:
          ans += 1


print(ans)