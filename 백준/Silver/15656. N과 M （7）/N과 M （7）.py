import sys
input = sys.stdin.readline

def perm(level):
    if level == M:
        print(*used)
        return
    
    for i in range(N):
        used[level] = lst[i]
        perm(level + 1)

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
used = [0] * M

perm(0)