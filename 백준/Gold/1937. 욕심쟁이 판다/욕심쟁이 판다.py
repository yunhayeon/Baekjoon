import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]


def dfs(i, j):
    if visited[i][j]:
        return visited[i][j]
    
    visited[i][j] = 1
    
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]

        if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] > lst[i][j]:
            visited[i][j] = max(visited[i][j], dfs(ni, nj) + 1)

    return visited[i][j]


for r in range(N):
    for c in range(N):
        dfs(r, c)

ans = 0
for v in visited:
    ans = max(ans, max(v))

print(ans)