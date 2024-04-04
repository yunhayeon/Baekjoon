from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(N)]

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][1] = 1
q = deque([(0, 0, 1)])
ans = -1

while q:
    i, j, canBreak = q.popleft()

    if (i, j) == (N - 1, M - 1):
        ans = visited[i][j][canBreak]
        break

    for d in range(4):
        ni, nj = i + di[d], j + dj[d]

        if 0 <= ni < N and 0 <= nj < M:
            if lst[ni][nj] == '0' and not visited[ni][nj][canBreak]:
                visited[ni][nj][canBreak] = visited[i][j][canBreak] + 1
                q.append((ni, nj, canBreak))

            elif lst[ni][nj] == '1' and canBreak:
                visited[ni][nj][0] = visited[i][j][1] + 1
                q.append((ni, nj, 0))

print(ans)