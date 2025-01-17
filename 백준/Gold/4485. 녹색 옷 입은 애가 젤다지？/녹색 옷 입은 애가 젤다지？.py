import heapq
import sys
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = 0

while True:
  T += 1
  N = int(input())

  if not N:
    break

  lst = [list(map(int, input().split())) for _ in range(N)]
  visited = [[float('inf') for _ in range(N)] for _ in range(N)]
  visited[0][0] = lst[0][0]
  pq = [(lst[0][0], 0, 0)]

  while pq: 
    sum, i, j = heapq.heappop(pq)

    if sum > visited[i][j]:
      continue

    for d in range(4):
      ni, nj = i + di[d], j + dj[d]

      if 0 <= ni < N and 0 <= nj < N:
        new = sum + lst[ni][nj]

        if visited[ni][nj] > new:
          visited[ni][nj] = new
          heapq.heappush(pq, (new, ni, nj))

  print(f'Problem {T}: {visited[- 1][- 1]}')