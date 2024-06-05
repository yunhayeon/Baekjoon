import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()
ans = -1

for i in range(N - 1):
    for j in range(i + 1, N):
        dif = lst[j] - lst[i]
        if dif >= M:
            if ans == -1:
                ans = dif
            else:
                ans = min(dif, ans)
            break
    
    if ans == M:
        break

print(ans)