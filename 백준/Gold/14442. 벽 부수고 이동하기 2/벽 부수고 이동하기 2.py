from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M, K = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(N)]

visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K + 1)]
visited[0][0][0] = 1
q = deque([(0, 0, 0, 1)])
ans = -1

while q:
    layer, i, j, cnt  = q.popleft()

    if (i, j) == (N - 1, M - 1):
        ans = cnt
        break

    for d in range(4):
        ni, nj = i + di[d], j + dj[d]

        if 0 <= ni < N and 0 <= nj < M:
            if lst[ni][nj] == '0' and not visited[layer][ni][nj]:
                visited[layer][ni][nj] = 1
                q.append((layer, ni, nj, cnt + 1))

            elif lst[ni][nj] == '1' and layer < K and not visited[layer + 1][ni][nj]:
                visited[layer + 1][ni][nj] = 1
                q.append((layer + 1, ni, nj, cnt + 1))

print(ans)