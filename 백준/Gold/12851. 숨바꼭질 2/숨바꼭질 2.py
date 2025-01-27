from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001
q = deque([N])
time, cnt = 100001, 0

while q:
  now = q.popleft()

  if visited[now] > time:
    break

  if now == K:
    if time == 100001:
      time = visited[now]
    
    if visited[now] == time:
      cnt += 1
    continue

  for next in [now - 1, now + 1, now * 2]:
    if 0 <= next <= 100000:
      if not visited[next] or visited[next] == visited[now] + 1:
        q.append(next)
        visited[next] = visited[now] + 1

print(time)
print(cnt)