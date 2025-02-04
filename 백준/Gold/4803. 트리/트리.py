from collections import deque
import sys
input = sys.stdin.readline

def dfs(n, lst):
  visited = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
  visit = [0 for _ in range(n + 1)]
  cnt = 0

  for i in range(1, n + 1):
    if not visit[i]:
      visit[i] = 1
      q = deque([i])
      isTree = True

      while q:
        now = q.popleft()

        for next in lst[now]:
          if not visited[now][next]:
            if not visit[next]:
              visited[now][next] = 1
              visited[next][now] = 1
              visit[next] = 1
              q.append(next)
            else:
              isTree = False

      if isTree:
        cnt += 1

  return cnt


tc = 1

while True:
  n, m = map(int, input().split())

  if not (n or m):
    break

  lst = [[] for _ in range(n + 1)]

  for _ in range(m):
    p1, p2 = map(int, input().split())
    lst[p1].append(p2)
    lst[p2].append(p1)

  # 트리 개수 세는 로직 
  tree = dfs(n, lst)

  if not tree:
    print(f'Case {tc}: No trees.')
  elif tree == 1:
    print(f'Case {tc}: There is one tree.')
  else:
    print(f'Case {tc}: A forest of {tree} trees.')

  tc += 1