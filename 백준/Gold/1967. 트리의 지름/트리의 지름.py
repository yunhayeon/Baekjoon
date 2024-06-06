from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, c, d = map(int, input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))

def bfs(s):
    visited = [-1] * (N + 1)
    visited[s] = 0
    q = deque([s])

    while q:
        now = q.popleft()
        for next, nd in tree[now]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[now] + nd

    maxi = max(visited)
    return (visited.index(maxi), maxi)

print(bfs(bfs(1)[0])[1])