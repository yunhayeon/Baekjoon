from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N):
    lst = list(map(int, input().split()))
    
    for i in range(1, len(lst) - 1, 2):
        tree[lst[0]].append((lst[i], lst[i + 1]))

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