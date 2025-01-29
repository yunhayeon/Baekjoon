from collections import deque
import sys
input = sys.stdin.readline

# 동, 남, 서, 북 | 시계 방향
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 위, 북, 동, 서, 남, 아래
dice = [1, 2, 3, 4, 5, 6]
visited = [[0 for _ in range(M)] for _ in range(N)]
d, ans = 0, 0
i, j = 0, 0


def roll(d):
  global dice

  if d == 0:
    dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
  elif d == 1:
    dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
  elif d == 2:
    dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
  elif d == 3:
    dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]


def bfs(r, c):
  global ans, visited

  if not visited[r][c]:
    visited[r][c] = 1
    q = deque([(r, c)])
    visit = [(r, c)]

    while q:
      y, x = q.popleft()

      for nd in range(4):
        ny, nx = y + di[nd], x + dj[nd]

        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and lst[ny][nx] == lst[r][c]:
          visited[ny][nx] = 1
          q.append((ny, nx))
          visit.append((ny, nx))

    counted = len(visit)

    for ci, cj in visit:
      visited[ci][cj] = counted

    ans += counted * lst[r][c]

  else:
    ans += visited[r][c] * lst[r][c]


for _ in range(K):
  ni, nj = i + di[d], j + dj[d]

  if not (0 <= ni < N and 0 <= nj < M):
    d = (d + 2) % 4
    ni, nj = i + di[d], j + dj[d]

  roll(d)
  bfs(ni, nj)

  if dice[5] > lst[ni][nj]:
    d = (d + 1) % 4
  elif dice[5] < lst[ni][nj]:
    d = (d - 1) % 4

  i, j = ni, nj


print(ans)