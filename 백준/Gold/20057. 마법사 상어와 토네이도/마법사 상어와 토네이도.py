import sys
input = sys.stdin.readline

# di : y / dj = x
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

# (x, y, %)
side = [
    (0, -2, 0.02), 
    (-1, -1, 0.1), (0, -1, 0.07), (1, -1, 0.01),
    (-2, 0, 0.05),
    (-1, 1, 0.1), (0, 1, 0.07), (1, 1, 0.01),
    (0, 2, 0.02),
    (-1, 0, 0),
]

# 방향별 x, y 좌표 변환
x = [(1, 1), (1, -1), (-1, 1), (-1, 1)]

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
i, j = N // 2, N // 2
ans = 0

d = 0       # 방향
dtc = 1     # 거리  
changeD = 0 # 바꾼 횟수

def tornado():
    global d, dtc, changeD, i, j, ans

    for _ in range(dtc):
        i, j = i + di[d], j + dj[d]
        if j == -1:
            return
        
        if lst[i][j]:
            now = lst[i][j]
            for sj, si, percent in side:
                if (d % 2):
                    sj, si = si, sj
                next = int(lst[i][j] * percent)
                ni, nj = i + si * x[d][1], j + sj * x[d][0]
                
                if 0 <= ni < N and 0 <= nj < N:
                    if percent != 0:
                        lst[ni][nj] += next
                        now -= next
                    else:
                        lst[ni][nj] += now
                else:
                    if percent != 0:
                        ans += next
                        now -= next
                    else:
                        ans += now

        lst[i][j] = 0

    d = (d + 1) % 4
    changeD += 1
    if changeD == 2:
        dtc += 1
        changeD = 0

    tornado()

tornado()
print(ans)