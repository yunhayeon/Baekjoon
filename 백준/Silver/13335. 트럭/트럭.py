import sys
input = sys.stdin.readline

# n: 트럭 수, w: 다리 길이, l: 다리 최대 하중
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

t = 0
idx = 0
bridge = [0 for _ in range(w)]

while True:
  if idx == n and sum(bridge) == 0:
    break

  t += 1
  bridge.pop(0)

  if idx < n and sum(bridge) + trucks[idx] <= l:
    bridge.append(trucks[idx])
    idx += 1
  else:
    bridge.append(0)

print(t)