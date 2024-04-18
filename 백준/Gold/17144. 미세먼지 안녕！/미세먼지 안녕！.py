import sys
input = sys.stdin.readline

# 시계 방향 : 우상좌하
di_up = [0, 1, 0, -1]
dj_up = [1, 0, -1, 0]

# 반시계 방향 : 우하좌상
di_down = [0, -1, 0, 1]
dj_down = [1, 0, -1, 0]

R, C, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(R)]
airCleaner = []
ans = 2

for r in range(R):
    if lst[r][0] == -1:
        airCleaner.append((r, 0))


# 1. 미세먼지 확산
def spreadFineDust():
    willChange = []

    for i in range(R):
        for j in range(C):
            if lst[i][j] > 0:
                side = lst[i][j] // 5

                if side:
                    possibleD = 0
                    for d in range(4):
                        ni, nj = i + di_up[d], j + dj_up[d]
                        if 0 <= ni < R and 0 <= nj < C and lst[ni][nj] != -1:
                            possibleD += 1
                            willChange.append((ni, nj, side))

                    lst[i][j] -= side * possibleD

    for ci, cj, c in willChange:
        lst[ci][cj] += c


def circle(i, j, di, dj):
    last = 0
    for d in range(4):
        while True:
            ni, nj = i + di[d], j + dj[d]

            if 0 <= ni < R and 0 <= nj < C and lst[ni][nj] != -1:
                i, j = ni, nj
                now = lst[ni][nj]
                lst[ni][nj] = last
                last = now
            else:
                break


# 2. 공기청정기 가동
def airCirculation():
    circle(airCleaner[0][0], airCleaner[0][1], di_down, dj_down)
    circle(airCleaner[1][0], airCleaner[1][1], di_up, dj_up)


for _ in range(T):
    spreadFineDust()
    airCirculation()

for l in lst:
    ans += sum(l)

print(ans)