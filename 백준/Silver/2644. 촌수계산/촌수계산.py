from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
per1, per2 = map(int, input().split())
m = int(input())
lst = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)


def bfs():
    visited = [-1 for _ in range(n + 1)]
    visited[per1] = 0
    q = deque([per1])

    while q:
        now = q.popleft()

        for next in lst[now]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[now] + 1

    return visited[per2]

print(bfs())