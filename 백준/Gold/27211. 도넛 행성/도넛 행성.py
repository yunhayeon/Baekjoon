import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
lst = []
area = 0

for _ in range(N):
    lst.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            area += 1
            q = [(i, j)]
            lst[i][j] = 1

            while q:
                r, c = q.pop()

                for d in range(4):
                    nr, nc = (r + dr[d]) % N, (c + dc[d]) % M

                    if lst[nr][nc] == 0:
                        q.append((nr, nc))
                        lst[nr][nc] = 1

print(area)