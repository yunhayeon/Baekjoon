from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

M, N, K = map(int, input().split())
lst = [[0] * M for _ in range(N)]

for _ in range(K):
    si, sj, ei, ej = map(int, input().split())
    for i in range(si, ei):
        for j in range(sj, ej):
            lst[i][j] = 1

q = deque()
cnt = 0
cnt_lst = deque()

for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            cnt += 1
            cnt_part = 1
            lst[i][j] = 1
            q.append((i, j))

            while q:
                size = len(q)

                for _ in range(size):
                    r, c = q.popleft()
                    for d in range(4):
                        nr, nc = r + di[d], c + dj[d]
                        if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] == 0:
                            lst[nr][nc] = 1
                            cnt_part += 1
                            q.append((nr, nc))

            cnt_lst.append(cnt_part)

print(cnt)
print(*sorted(cnt_lst))