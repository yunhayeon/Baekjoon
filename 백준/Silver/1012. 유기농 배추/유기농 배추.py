from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    lst = [[0] * M for _ in range(N)]
    q = deque()
    cnt = 0

    for _ in range(K):
        c, r = map(int, input().split())
        lst[r][c] = 1

    for r in range(N):
        for c in range(M):
            if lst[r][c] == 1:
                cnt += 1
                lst[r][c] = 0
                q.append((r, c))

                while q:
                    i, j = q.popleft()

                    for d in range(4):
                        ni = i + di[d]
                        nj = j + dj[d]
                        if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 1:
                            lst[ni][nj] = 0
                            q.append((ni, nj))

    print(cnt)
