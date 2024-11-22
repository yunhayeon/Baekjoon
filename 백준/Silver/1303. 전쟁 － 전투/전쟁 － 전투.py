from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
visited = [[0 for _ in range(N)] for _ in range(M)]
teamW = 0
teamB = 0
lst = []

for _ in range(M):
    lst.append(list(input().rstrip()))

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            total = 1
            visited[i][j] = 1
            q = deque([(i, j)])

            while q:
                r, c = q.popleft()

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and lst[i][j] == lst[nr][nc]:
                        total += 1
                        visited[nr][nc] = 1
                        q.append((nr, nc))

            if lst[i][j] == 'W':
                teamW += total ** 2
            else:
                teamB += total ** 2

print(teamW, teamB)