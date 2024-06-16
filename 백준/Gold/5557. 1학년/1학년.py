import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [[0 for _ in range(21)] for _ in range(N - 1)]

dp[0][lst[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j]:
            add = j + lst[i]
            min = j - lst[i]

            if add <= 20:
                dp[i][add] += dp[i - 1][j]
            if min >= 0:
                dp[i][min] += dp[i - 1][j]

print(dp[-1][lst[-1]])