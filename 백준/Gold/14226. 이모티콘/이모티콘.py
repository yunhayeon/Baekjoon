import sys
input = sys.stdin.readline

S = int(input())
q = [(1, 0)]
visited = [[0 for _ in range(2000)] for _ in range(2000)]
visited[1][0] = 1
find = False
t = 0

while True:
  nq = []

  for now, db in q:
    if now == S:
      find = True
      break

    if now < 2000 and not visited[now][now]:
      visited[now][now] = 1
      nq.append((now, now))

    if db:
      next = now + db
      if next < 2000 and not visited[next][db]:
        visited[next][db] = 1
        nq.append((next, db))

    if now and not visited[now - 1][db]:
      visited[now - 1][db] = 1
      nq.append((now - 1, db))

  if find:
    break

  q = nq
  t += 1


print(t)
