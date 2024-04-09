from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
wall = []
virus = []
ans = 0

for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            wall.append((i, j))

        elif lst[i][j] == 2:
            virus.append((i, j))

def bfs():
    global ans

    v = deque(virus[:])
    changed = []
    cnt = 0

    while v:
        r, c = v.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] == 0:
                lst[nr][nc] = 2
                v.append((nr, nc))
                changed.append((nr, nc))

    for l in lst:
        cnt += l.count(0)

    if ans < cnt:
        ans = cnt

    for r, c in changed:
        lst[r][c] = 0


def perm(level, idx):
    if level == 3:
        bfs()
        return

    for i in range(idx, len(wall)):
        lst[wall[i][0]][wall[i][1]] = 1
        perm(level + 1, i + 1)
        lst[wall[i][0]][wall[i][1]] = 0

perm(0, 0)
print(ans)