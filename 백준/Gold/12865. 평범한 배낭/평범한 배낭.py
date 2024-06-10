import sys
input = sys.stdin.readline

N, K = map(int, input().split())
used = [[0] * (K + 1) for _ in range(N + 1)]
lst = []

for _ in range(N):
    W, V = map(int, input().split())
    lst.append([W, V])

for i in range(N):
    for j in range(1, K + 1):
        w, v = lst[i][0], lst[i][1]

        if w <= j:
            used[i + 1][j] = max(used[i][j], used[i][j - w] + v)
        else:
            used[i + 1][j] = used[i][j]

print(used[-1][-1])