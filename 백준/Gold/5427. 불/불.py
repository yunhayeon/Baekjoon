from collections import deque
import sys
input = sys.stdin.readline
from pprint import pprint

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for _ in range(T):

  w, h = map(int, input().split())
  lst = [list(input().rstrip()) for _ in range(h)]

  visited = [[0 for _ in range(w)] for _ in range(h)]
  now = deque([])
  fire = deque([])
  find = False
  ans = 1

  for i in range(h):
    for j in range(w):
      if lst[i][j] == '#':
        visited[i][j] = 3
      
      elif lst[i][j] == '@':
        visited[i][j] = 1
        now.append((i, j))

      elif lst[i][j] == '*':
        visited[i][j] = 2
        fire.append((i, j))

  while True:
    if not now:
      ans = 'IMPOSSIBLE'
      break

    nl = len(now)
    for _ in range(nl):
      i, j = now.popleft()

      for d in range(4):
        ni, nj = i + di[d], j + dj[d]

        if 0 <= ni < h and 0 <= nj < w:
          if visited[i][j] == 1 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            now.append((ni, nj))
        else:
          if visited[i][j] == 1:
            find = True
            break

      if find:
        break

    if find:
      break

    fl = len(fire)
    for _ in range(fl):
      i, j = fire.popleft()

      for d in range(4):
        ni, nj = i + di[d], j + dj[d]

        if 0 <= ni < h and 0 <= nj < w:
          if visited[ni][nj] <= 1:
            visited[ni][nj] = 2
            fire.append((ni, nj))

    ans += 1

  print(ans)