from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
virus = []
ans = -1
counter = 0

for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            lst[i][j] = -1
            virus.append((i, j))


def bfs(use):
    global ans

    q = deque(use)
    change = []
    change_v = []
    cnt = 0
    safe = 0
    counter = 0

    while q:
        cnt += 1
        size = len(q)

        for _ in range(size):
            r, c = q.popleft()
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:

                    if lst[nr][nc] == 0:
                        lst[nr][nc] = 2
                        q.append((nr, nc))
                        change.append((nr, nc))
                        counter = cnt

                    elif lst[nr][nc] == -1:
                        lst[nr][nc] = 2
                        q.append((nr, nc))
                        change_v.append((nr, nc))

    for l in lst:
        safe += l.count(0)

    for i, j, in change:
        lst[i][j] = 0

    for i, j in change_v:
        lst[i][j] = -1

    if not safe:
        if ans == -1:
            ans = counter
        else:
            ans = min(ans, counter)


def perm(level, idx, used):
    if level == M:
        bfs(used)
        return

    for n in range(idx, len(virus)):
        lst[virus[n][0]][virus[n][1]] = 2
        perm(level + 1, n + 1, used + [virus[n]])
        lst[virus[n][0]][virus[n][1]] = -1


perm(0, 0, [])

print(ans)