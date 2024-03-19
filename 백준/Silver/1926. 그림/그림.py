from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
q = deque()
ans = 0
cnt = 0

for r in range(n):
    for c in range(m):
        if lst[r][c] == 1:
            big = 1
            cnt += 1
            lst[r][c] = 0
            q.append((r, c))

            while q:
                size = len(q)
                for _ in range(size):
                    i, j = q.pop()
                    for d in range(4):
                        ni = i + di[d]
                        nj = j + dj[d]

                        if 0 <= ni < n and 0 <= nj < m and lst[ni][nj] == 1:
                            big += 1
                            lst[ni][nj] = 0
                            q.append((ni, nj))

            if big > ans:
                ans = big

print(cnt)
print(ans)