from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
sr, sc = 0, 0
shark = 2
eat = 0
total = 0


def start():
    global sr, sc

    for r in range(N):
        for c in range(N):
            if lst[r][c] == 9:
                lst[r][c] = 0
                sr, sc = r, c
                return


def bfs(si, sj):
    global shark, eat, total

    cnt = 0
    q = deque([(si, sj)])
    visited = [[0] * N for _ in range(N)]

    while q:
        cnt += 1
        canEat = []
        size = len(q)

        for _ in range(size):
            i, j = q.popleft()
            visited[i][j] = 1

            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < N and 0 <= nj < N:
                    if 0 < lst[ni][nj] < shark:
                        canEat.append((ni, nj))

                    elif (lst[ni][nj] == 0 or lst[ni][nj] == shark) and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        q.append((ni, nj))

        if canEat:
            canEat.sort()
            lst[canEat[0][0]][canEat[0][1]] = 0
            eat += 1
            total += cnt
            if eat == shark:
                eat = 0
                shark += 1
            return bfs(canEat[0][0], canEat[0][1])

    return


start()
bfs(sr, sc)

print(total)