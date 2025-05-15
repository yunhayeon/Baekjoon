import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
tree = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
visited[1] = 1

for _ in range(M):
  a, b = map(int, input().split())

  tree[a].append(b)
  tree[b].append(a)

for i in tree[1]:
  visited[i] = 1

  for j in tree[i]:
    visited[j] = 1

print(visited.count(1) - 1)