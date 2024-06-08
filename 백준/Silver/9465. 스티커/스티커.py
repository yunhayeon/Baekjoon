import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    t = list(map(int, input().split()))
    b = list(map(int, input().split()))
    maxi = 0

    if N > 1:
        t[1] += b[0]
        b[1] += t[0]

    for i in range(2, N):
        t[i] += max(b[i - 1], b[i - 2])
        b[i] += max(t[i - 1], t[i - 2])

    print(max(max(t), max(b)))