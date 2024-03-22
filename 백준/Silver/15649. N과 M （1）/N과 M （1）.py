import sys
input = sys.stdin.readline

def perm(level, used):
    if level == M:
        print(*used)
        return

    for i in range(N):
        if num[i] not in used:
            perm(level + 1, used + [num[i]])

N, M = map(int, input().split())
num = [i for i in range(1, N + 1)]

perm(0, [])