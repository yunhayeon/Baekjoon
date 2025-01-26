import sys
input = sys.stdin.readline

N = int(input())
l = len(str(N)) - 1
ans = 0

for i in range(l):
    ans += 9 * (10 ** i) * (i + 1)

ans += (N - 10 ** l + 1) * (l + 1)

print(ans)