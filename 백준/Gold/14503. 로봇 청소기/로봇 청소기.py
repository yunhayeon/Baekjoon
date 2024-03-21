import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

# 2 : 청소한 칸
while True:
    if lst[r][c] == 0:
        lst[r][c] = 2
        cnt += 1

    for k in range(4):
        d = (d + 3) % 4
        nr = r + di[d]
        nc = c + dj[d]
        if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] == 0:
            r, c = nr, nc
            break
    
    else:
        back = (d + 2) % 4
        br = r + di[back]
        bc = c + dj[back]
        if 0 <= br < N and 0 <= bc < M and lst[br][bc] != 1:
            r, c = br, bc
        else:
            break

print(cnt)