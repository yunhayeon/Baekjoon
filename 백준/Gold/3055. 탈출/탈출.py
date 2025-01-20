from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

R, C = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]   # 물이 갈 수 없는 좌표
now = []      # 고슴도치의 좌표
water = []    # 물의 좌표
flag = 0
cnt = 0

for i in range(R):
    for j in range(C):
        if lst[i][j] == 'S':
            now.append((i, j))

        elif lst[i][j] == '*':
            water.append((i, j))
            visited[i][j] = 1

        elif lst[i][j] == 'X':
            visited[i][j] = 1

while True:
    cnt += 1

    next = []
    while now:
        i, j = now.pop()
        if lst[i][j] == 'S':
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < R and 0 <= nj < C:
                    if lst[ni][nj] == 'D':
                        flag = 1
                        now = []
                        break

                    elif lst[ni][nj] == '.':
                        lst[ni][nj] = 'S'
                        next.append((ni, nj))
    
    if flag:
        break
    
    if next:
        now = next
    else:
        cnt = 'KAKTUS'
        break

    toWater = []
    while water:
        i, j = water.pop()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < R and 0 <= nj < C and lst[ni][nj] != 'D' and not visited[ni][nj]:
                lst[ni][nj] = '*'
                visited[ni][nj] = 1
                toWater.append((ni, nj))

    water = toWater

print(cnt)