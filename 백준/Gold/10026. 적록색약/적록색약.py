from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N = int(input())
lst = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
notRGB = [[0] * N for _ in range(N)]
cnt1, cnt2 = 0, 0

for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            cnt1 += 1
            visited[r][c] = 1
            q = deque([(r, c)])

            while q:
                i, j = q.popleft()
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]

                    if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == lst[r][c] and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        q.append((ni, nj))

        if not notRGB[r][c]:
            cnt2 += 1
            notRGB[r][c] = 1
            qq = deque([(r, c)])

            while qq:
                i, j = qq.popleft()
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]

                    if 0 <= ni < N and 0 <= nj < N and not notRGB[ni][nj]:
                        if lst[r][c] == 'B' and lst[ni][nj] == 'B':
                            notRGB[ni][nj] = 1
                            qq.append((ni, nj))
                        elif lst[r][c] != 'B' and lst[ni][nj] != 'B':
                            notRGB[ni][nj] = 1
                            qq.append((ni, nj))
                        
print(cnt1, cnt2)