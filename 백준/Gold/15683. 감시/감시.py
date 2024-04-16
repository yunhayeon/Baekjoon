import sys
input = sys.stdin.readline

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
cctv = []
ans = -1


def drawing(i, j, d):
    k = 0
    change = []
    
    while True:
        k += 1
        ni, nj = i + di[d] * k, j + dj[d] * k

        if 0 <= ni < N and 0 <= nj < M:
            if lst[ni][nj] == 0:
                change.append((ni, nj))
                lst[ni][nj] = 9
            elif lst[ni][nj] == 6:
                break
        else:
            break

    return change


def count():
    global ans

    cnt = 0
    for l in lst:
        cnt += l.count(0)

    if ans == -1:
        ans = cnt
    elif ans > cnt:
        ans = cnt

def origin(chg):
    for r, c in chg:
        lst[r][c] = 0


for i in range(N):
    for j in range(M):
        if 0 < lst[i][j] < 5:
            cctv.append((lst[i][j], i, j))
        elif lst[i][j] == 5:
            for d in range(4):
                drawing(i, j, d)

cctv_total = len(cctv)

def perm(idx):
    if idx == cctv_total:
        count()
        return
    
    num, i, j = cctv[idx]

    if ans != 0:
        if num == 1:
            for d in range(4):
                chg = drawing(i, j, d)
                perm(idx + 1)
                origin(chg)

        elif num == 2:    
            for d in range(2):
                chg = []
                chg.extend(drawing(i, j, d))
                chg.extend(drawing(i, j, d + 2))
                perm(idx + 1)
                origin(chg)

        elif num == 3:
            for d in range(4):
                chg = []
                chg.extend(drawing(i, j, d))
                chg.extend(drawing(i, j, (d + 1) % 4))
                perm(idx + 1)
                origin(chg)

        elif num == 4:
            for d in range(4):
                chg = []
                chg.extend(drawing(i, j, (d + 1) % 4))
                chg.extend(drawing(i, j, (d + 2) % 4))
                chg.extend(drawing(i, j, (d + 3) % 4))
                perm(idx + 1)
                origin(chg)


perm(0)
print(ans)