from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]
num = [i for i in range(N)]
lst = list(map(int, input().split()))
start = 0
cnt = 0

for i in range(N):
    if lst[i] != -1:
        tree[lst[i]].append(num[i])
    else:
        start = num[i]

target = int(input())


def bfs(s, t, N):
    global cnt

    visited = [0] * (N + 1)
    visited[s] = 1
    visited[t] = 1
    q = deque([s])

    while q:
        now = q.popleft()
        
        if len(tree[now]) == 0:
            cnt += 1
        
        for next in tree[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = 1
            elif len(tree[now]) == 1 and next == target:
                cnt += 1

if start != target:
    bfs(start, target, N)

print(cnt)