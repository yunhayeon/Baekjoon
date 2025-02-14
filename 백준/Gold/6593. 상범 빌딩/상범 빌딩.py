from collections import deque
import sys
input = sys.stdin.readline

di = [0, 1, 0, -1, 0, 0]
dj = [1, 0, -1, 0, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

while True:
  L, R, C = map(int, input().split())
  if not (L or R or C):
    break

  q = deque([])
  find = False
  lst = []
  time = 0

  for k in range(L):
    floor = [list(input().rstrip()) for _ in range(R)]
    _ = input()

    lst.append(floor)

    for i in range(R):
      for j in range(C):
        if floor[i][j] == 'S':
          q.append((i, j, k))
          break

  while q:
    lq = len(q)
    time += 1

    for _ in range(lq):
      i, j, k = q.popleft()

      for d in range(6):
        ni, nj, nk = i + di[d], j + dj[d], k + dk[d]

        if 0 <= ni < R and 0 <= nj < C and 0 <= nk < L:
          if lst[nk][ni][nj] == '.':
            lst[nk][ni][nj] = '#'
            q.append((ni, nj, nk))

          elif lst[nk][ni][nj] == 'E':
            find = True
            break

      if find:
        q = deque([])
        break

  if find:
    print(f'Escaped in {time} minute(s).')
  else:
    print('Trapped!')