from collections import deque
import sys
input = sys.stdin.readline


def bfs(s, e, N):
    visited = [0] * (N + 1)
    visited[s] = 1
    q = deque([(s, 0)])

    while q:
        now, dtc = q.popleft()
        if now == e:
            print(dtc)
            return

        for next in tree[now]:
            if not visited[next]:
                q.append((next, dtc + dis[now][next]))
                visited[next] = 1


N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
dis = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N - 1):
    s, e, d = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
    dis[s][e] = d
    dis[e][s] = d

for _ in range(M):
    start, end = map(int, input().split())
    bfs(start, end, N)

