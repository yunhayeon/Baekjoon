import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(i, j, cnt):
    global ans

    for d in range(4):
        ni, nj = i + di[d], j + dj[d]

        if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj]:
            num = ord(lst[ni][nj]) - 65
            if used[num] == 0:
                visited[ni][nj] = 1
                used[num] = 1
                dfs(ni, nj, cnt + 1)
                visited[ni][nj] = 0
                used[num] = 0

    if ans < cnt:
        ans = cnt

R, C = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
visited[0][0] = 1
used = [0] * 26
used[ord(lst[0][0]) - 65] = 1
ans = 0
dfs(0, 0, 1)

print(ans)