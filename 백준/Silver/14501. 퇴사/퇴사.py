import sys
input = sys.stdin.readline

# level : day(=idx) / end : 남은 상담일 / money : 최종 금액
def recur(level, end, money):
    global maxi

    if level == N:
        if maxi < money:
            maxi = money
        return
    
    if end > 0:
        recur(level + 1, end - 1, money)
    else:
        if level + lst[level][0] <= N:
            recur(level + 1, lst[level][0] - 1, money + lst[level][1])
            recur(level + 1, 0, money)
        else:
            recur(level + 1, 0, money)


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
maxi = 0

recur(0, 0, 0)
print(maxi)