import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def calScore(used):
    global ans

    now = 0
    score = 0

    for j in range(N):
        out = 0
        b1, b2, b3 = 0, 0, 0

        while out < 3:
            if lst[j][used[now]] == 0:
                out += 1
            elif lst[j][used[now]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif lst[j][used[now]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif lst[j][used[now]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif lst[j][used[now]] == 4:
                score += 1 + b1 + b2 + b3
                b1, b2, b3 = 0, 0, 0

            now = (now + 1) % 9

    if ans < score:
        ans = score


def perm(level, used):
    if level == 9:
        calScore(used)
        return

    for i in range(1, 9):
        if i not in used:
            if level == 3:
                level += 1

            used[level] = i
            perm(level + 1, used)
            used[level] = -1

used = [-1] * 9
used[3] = 0
perm(0, used)

print(ans)