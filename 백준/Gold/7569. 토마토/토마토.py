from collections import deque
import sys
input = sys.stdin.readline

# 1차원 시계방향 + 위아래
di = [-1, 0, 1, 0, 0, 0]
dj = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if lst[h][i][j] == 1:
                q.append((h, i, j))

def bfs():
    cnt = 0
    ans = 0

    while q:
        size = len(q)
        cnt += 1

        for _ in range(size):
            h, i, j = q.popleft()

            for d in range(6):
                nh = h + dh[d]
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and lst[nh][ni][nj] == 0:
                    lst[nh][ni][nj] = 1
                    q.append((nh, ni, nj))
    
    else:
        for x in lst:
            for y in x:
                if 0 in y:
                    ans = -1
                    break
            if ans == -1:
                break

        else:
            ans = cnt - 1

    return ans

print(bfs())