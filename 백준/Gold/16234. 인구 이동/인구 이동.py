from collections import deque
import sys
import math
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, L, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
pq = deque()
q = deque()
sum = deque()

while True:
    visited = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                pq.append((r, c))
                visited[r][c] = 1
                psum = 0
                rq = []

                while pq:
                    size = len(pq)

                    for _ in range(size):
                        i, j = pq.popleft()

                        for d in range(4):
                            ni = i + di[d]
                            nj = j + dj[d]
                            
                            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(lst[i][j] - lst[ni][nj]) <= R:
                                if psum == 0:
                                    psum = lst[i][j]
                                    rq.append((i, j))

                                pq.append((ni, nj))
                                rq.append((ni, nj))
                                psum += lst[ni][nj]
                                visited[ni][nj] = 1

                if rq:
                    q.append(rq)
                    sum.append(psum)

    if q:
        cnt += 1
        while q:
            size = len(q)

            for _ in range(size):
                area = q.popleft()
                new = math.floor(sum.popleft() / len(area))

                for r, c in area:
                    lst[r][c] = new

    else:
        print(cnt)
        break