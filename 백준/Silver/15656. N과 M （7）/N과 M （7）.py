import sys
input = sys.stdin.readline

def perm(level, used):
    if level == M:
        print(*used)
        return
    
    for i in range(N):
        perm(level + 1, used + [lst[i]])

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

perm(0, [])