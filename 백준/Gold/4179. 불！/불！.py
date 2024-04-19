from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

R, C = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(R)]
now = deque()
fire = deque()
cnt = 0
ans = 0

for r in range(R):
    for c in range(C):
        if lst[r][c] == 'J':
            now.append((r, c))
        elif lst[r][c] == 'F':
            fire.append((r, c))

while True:
    cnt += 1
    sizeNow = len(now)
    sizeFire = len(fire)

    if not now:
        ans = 'IMPOSSIBLE'
        break

    for _ in range(sizeNow):
        i, j = now.popleft()
        if lst[i][j] == 'J':
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < R and 0 <= nj < C: 
                    if lst[ni][nj] == '.':
                        lst[ni][nj] = 'J'
                        now.append((ni, nj))
                else:
                    ans = cnt
                    break

    if ans != 0:
        break

    for _ in range(sizeFire):
        i, j = fire.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < R and 0 <= nj < C and (lst[ni][nj] == '.' or lst[ni][nj] == 'J'):
                lst[ni][nj] = 'F'
                fire.append((ni, nj))

print(ans)