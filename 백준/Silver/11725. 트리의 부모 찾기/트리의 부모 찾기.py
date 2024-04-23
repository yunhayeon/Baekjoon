import sys
input = sys.stdin.readline

def dfs(v, N):
    visited = [0] * (N + 1)
    visited[v] = 1
    i = v
    stack = []

    while True:
        for j in tree[i]:
            if not visited[j]:
                stack.append(i)
                visited[j] = i
                i = j
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break

    for v in range(2, N + 1):
        print(visited[v])


N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p1, p2 = map(int, input().split())
    tree[p1].append(p2)
    tree[p2].append(p1)

dfs(1, N)