from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
road = list(map(int, input().split()))

tree = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
visited[road[0]] = 1
q = deque([road[0]])
ans = 'YES'

for i in range(N):
  for j in range(N):
    if lst[i][j]:
      tree[i + 1].append(j + 1)

while q:
  now = q.popleft()

  for next in tree[now]:
    if not visited[next]:
      visited[next] = 1
      q.append(next)

for r in road:
  if not visited[r]:
    ans = 'NO'
    break

print(ans)