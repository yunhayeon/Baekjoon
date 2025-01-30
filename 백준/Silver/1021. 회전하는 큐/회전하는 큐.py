from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = deque(list(map(int, input().split())))

dq = deque([i for i in range(1, N + 1)])
ans = 0

for l in lst:
  if l == dq[0]:
    dq.popleft()
    continue
  
  i = dq.index(l)
  ldq = len(dq)

  if i <= ldq // 2:
    dq.rotate(-i)
    ans += i
  else:
    dif = ldq - i
    dq.rotate(dif)
    ans += dif

  dq.popleft()

print(ans)