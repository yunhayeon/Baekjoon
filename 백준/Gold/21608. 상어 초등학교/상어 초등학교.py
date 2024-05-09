import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}

N = int(input())
N2 = N * N
students = []
liked = [[] for _ in range(N2 + 1)]
seat = [[0] * N for _ in range(N)]

for _ in range(N2):
    std, *like = map(int, input().split())
    students.append(std)
    liked[std] = like

def findSeat(std):
    canSeat = []

    for i in range(N):
        for j in range(N):

            if seat[i][j] == 0:
                around = 4
                empty = 4

                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]

                    if 0 <= ni < N and 0 <= nj < N:
                        if seat[ni][nj] in liked[std]:
                            around -= 1
                        if seat[ni][nj] == 0:
                            empty -= 1
                
                canSeat.append((around, empty, i, j))

    canSeat.sort(key= lambda x: (x[0], x[1], x[2], x[3]))
    seat[canSeat[0][2]][canSeat[0][3]] = std
    

for student in students:
    findSeat(student)

ans = 0
for r in range(N):
    for c in range(N):
        std = seat[r][c]
        cnt = 0
        for d in range(4):
            nr, nc = r + di[d], c + dj[d]
            if 0 <= nr < N and 0 <= nc < N and seat[nr][nc] in liked[std]:
                cnt += 1

        ans += score[cnt]

print(ans)