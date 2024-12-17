from collections import deque
import sys
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]
xylen = N + M - 2
qlen = xylen * 2
i, j, d = 0, 0, 0
q = deque([])
point = []


def rotateQ():
    global q, xylen, qlen, visited, point

    t = R % qlen
    q.rotate(-t)

    for idx, (r, c) in enumerate(point):
        visited[r][c] = q[idx]

    q = deque([])
    point = []
    xylen -= 4
    qlen = xylen * 2


for _ in range(N * M):
    q.append(lst[i][j])
    point.append((i, j))
    visited[i][j] = 1

    ni = i + di[d]
    nj = j + dj[d]

    if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
        i, j = ni, nj
    else:
        d = (d + 1) % 4
        i = i + di[d]
        j = j + dj[d]

    # 회전
    if len(q) == qlen:
        rotateQ()


for l in range(N):
    print(*visited[l])