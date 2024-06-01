import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, Q = map(int, input().split())
line = 2 ** N
lst = []

for _ in range(line):
    lst.append(list(map(int, input().split())))

ipt = list(map(int, input().split()))

# 슬라이싱한 부분 배열 90도 회전
def rotate90(nl, part):
    new = [[0] * nl for _ in range(nl)]

    for i in range(nl):
        for j in range(nl):
            new[j][nl - i - 1] = part[i][j]

    return new

# 회전한 부분 배열 원본 배열에 저장
def savePart(r, c, nl, part):
    for n in range(nl):
        nr = n + r
        lst[nr] = lst[nr][:c] + part[n] + lst[nr][c + nl:]

# 얼음 녹이기
def meltingIce(line):
    change = []

    for i in range(line):
        for j in range(line):
            if lst[i][j]:
                cnt = 0
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < line and 0 <= nj < line and lst[ni][nj] > 0:
                        cnt += 1
                
                if cnt < 3:
                    change.append((i, j))

    for ci, cj in change:
        lst[ci][cj] -= 1


for ip in ipt:
    if ip > 0:
        size = ip
        newLine = 2 ** size
        time = line // newLine

        # 1. 90도 회전 및 저장
        for r in range(time):
            for c in range(time):
                part = []
                for l in range(newLine):
                    part.append(lst[newLine * r + l][newLine * c:newLine * c + newLine])

                part = rotate90(newLine, part)
                savePart(newLine * r, newLine * c, newLine, part)

    # 2. 얼음 녹이기
    meltingIce(line)

# 3. 남은 얼음 계산
cntAll = 0
for l in range(line):
    cntAll += sum(lst[l])

# 4. 가장 큰 넓이 구하기
areaAll = 0
for i in range(line):
    for j in range(line):
        if lst[i][j] != 0:
            area = 1
            q = [(i, j)]
            lst[i][j] = 0

            while q:
                ii, jj = q.pop()
                for d in range(4):
                    ni, nj = ii + di[d], jj + dj[d]

                    if 0 <= ni < line and 0 <= nj < line and lst[ni][nj] > 0:
                        q.append((ni, nj))
                        lst[ni][nj] = 0
                        area += 1

            if areaAll < area:
                areaAll = area

print(cntAll)
print(areaAll)