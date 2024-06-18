import sys
input = sys.stdin.readline

N = int(input())
used = [0 for _ in range(N + 1)]

for now in range(1, N + 1):
    T, P = map(int, input().split())

    used[now] = max(used[now - 1], used[now])

    next = now + T - 1
    if next <= N:
        used[next] = max(used[next], used[now - 1] + P)

print(used[-1])
