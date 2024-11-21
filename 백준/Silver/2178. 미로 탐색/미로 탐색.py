import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
lst = [list(map(int, list(input().rstrip()))) for _ in range(N)]
ei, ej = N - 1, M - 1


def bfs():
    q = [(0, 0)]
    lst[0][0] = 0
    cnt = 1

    while q:
        size = len(q)
        cnt += 1

        for _ in range(size):
            i, j = q.pop(0)

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 1:
                    if ni == ei and nj == ej:
                        q = []
                        break

                    lst[ni][nj] = 0
                    q.append((ni, nj))

                if ni == ei and nj == ej:
                    break

            if ni == ei and nj == ej:
                print(cnt)
                break

bfs()