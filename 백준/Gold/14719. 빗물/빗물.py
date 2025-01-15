import sys
input = sys.stdin.readline

H, W = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

for h in range(H - 1, -1, -1):
  wall = []
  for w in range(W):
    if lst[w] >= h + 1:
      wall.append(w)

  for i in range(1, len(wall)):
    dif = wall[i] - wall[i - 1] - 1
    if dif:
      ans += dif

print(ans)