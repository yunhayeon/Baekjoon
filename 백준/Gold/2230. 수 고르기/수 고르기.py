import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()
ans = int(2e9)

l, r = 0, 0

while l <= r and r < N:
    dif = lst[r] - lst[l]
    if dif < M:
        r += 1
    else:
        ans = min(ans, dif)
        l += 1
    
    if ans == M:
        break

print(ans)