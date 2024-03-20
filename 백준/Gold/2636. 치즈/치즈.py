from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

q = deque([(0, 0)])
side = deque()
history = deque()

cnt = 0
for y in range(N):
    for x in range(M):
        if lst[y][x] == 1:
            cnt += 1

history.append(cnt)

n = 2
while True:
    q = deque([(0, 0)])
    side = deque()
    cnt = 0

    while q:
        size = len(q)

        for _ in range(size):
            i, j = q.pop()
            lst[i][j] = n

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < N and 0 <= nj < M: 
                    if lst[ni][nj] == n - 2:
                        q.append((ni, nj))
                        lst[ni][nj] = n
                    if lst[ni][nj] == 1 and (ni, nj):
                        side.append((ni, nj))

    for i, j in side:
        lst[i][j] = n

    for r in range(N):
        for c in range(M):
            if lst[r][c] == 1:
                cnt += 1
            if lst[r][c] == n - 2:
                lst[r][c] = n

    history.append(cnt)
    n += 2

    if history[-1] == 0:
        print(len(history) - 1)
        print(history[-2])
        break