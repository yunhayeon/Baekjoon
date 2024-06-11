import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
known = list(map(int, input().split()))[1:]
know = []
tree = [[] for _ in range(N + 1)]
party = []
ans = 0

def bfs(s):
    visited = [0] * (N + 1)
    visited[s] = 1
    q = deque([s])

    while q:
        now = q.popleft()
        for next in tree[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = 1
                know.append(next)

for _ in range(M):
    p = list(map(int, input().split()))
    t = p[0]
    p = p[1:]
    party.append(p)

    for i in range(t):
        tree[p[i]] = list(set(tree[p[i]]) | set(p) - set([p[i]]))

for kn in known:
    bfs(kn)

known = set(known) | set(know)
    
for part in party:
    if not set(part) & known:
        ans += 1

print(ans)