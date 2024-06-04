import sys
input = sys.stdin.readline

N = int(input())
lst = [i for i in range(10)]
cnt = 0
ans = False

def backTracking(level, end, used):
    global cnt, ans

    if level == end:
        cnt += 1
        if cnt == N:
            ans = ''.join(list(map(str, used)))
        elif len(used) == 10:
            ans = -1
        return

    for i in range(10):
        if (used and used[-1] > i) or (not used) and cnt < N:
            backTracking(level + 1, end, used + [i])

numLen = 1
while True:
    backTracking(0, numLen, [])

    if ans != False:
        break

    numLen += 1

print(ans)